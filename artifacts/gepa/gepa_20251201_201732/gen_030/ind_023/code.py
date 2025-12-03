
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # A (root of next chord)
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.375),  # B (fifth)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # D (root of next chord)
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),  # E (fifth)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # F (root of next chord)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),  # F# (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # E (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Ab (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
])
# Bar 4: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C (Dm7)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
])
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - D - G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
