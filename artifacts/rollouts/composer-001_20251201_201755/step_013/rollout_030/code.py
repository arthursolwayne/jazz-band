
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (48) -> Gb (47) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    # Bar 2: C (60) -> B (59) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    # Bar 3: Ab (57) -> G (67) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    # Bar 3: D (62) -> Eb (61) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),
    # Bar 4: F (48) -> Gb (47) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    # Bar 4: C (60) -> B (59) chromatic approach to Fm7
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # F
    # Bar 3: Bbm7 (Bb, Db, F, Ab) - open voicing
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb
    # Bar 4: Eb7 (Eb, G, Bb, D) - open voicing
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625),  # E
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.375),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.625),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5)

# Add the drum notes to the drums instrument
# Wait, the loop above didn't actually append the notes. Let's fix that
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("jazz_intro.mid")
