
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=73, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0),   # G#2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.0),  # E
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.5),  # Ab
])

# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=3.0),  # Bb
])

for note in piano_notes:
    piano.notes.append(note)

# Dante: Sax, short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (78), Ab (80), Bb (81), F (78)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=78, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=80, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=81, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=2.5, end=2.75),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue
# Kick on 1 and 3 (beat 0 and 2)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
])

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
# Kick on 1 and 3 (beat 0 and 2)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
