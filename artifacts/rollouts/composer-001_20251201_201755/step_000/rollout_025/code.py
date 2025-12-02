
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A2 (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=3.0),  # D (MIDI 50)
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=3.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E (Dm7 3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # D (root)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875),  # E (resolve)
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # G (tension)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),  # C3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # D2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # G (MIDI 55)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=4.5),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, build tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # G (tension)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # E (resolve back to Dm)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # A2 (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # D (MIDI 50)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=6.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E (Dm7 3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # D (root)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # E (resolve)
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
