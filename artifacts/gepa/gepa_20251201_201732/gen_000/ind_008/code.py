
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: Walking line in F (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=80, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0),  # Bb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0), # E

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=3.0, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=4.5), # Ab

    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=6.0), # F#
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0), # C
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: Motif in F, one short phrase, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
