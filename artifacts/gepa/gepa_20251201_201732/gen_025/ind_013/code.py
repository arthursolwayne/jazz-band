
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F root (MIDI 48)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    # Bb (MIDI 50) chromatic approach from B (MIDI 51)
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=50, start=2.125, end=2.5),
    # C (MIDI 52)
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.875),
    # F root again
    pretty_midi.Note(velocity=100, pitch=48, start=2.875, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (MIDI 53), Ab (MIDI 56), Bb (MIDI 58), F (MIDI 53)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line continuing
bass_notes = [
    # Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    # G (MIDI 47) chromatic approach from G# (MIDI 48)
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=47, start=3.625, end=4.0),
    # C (MIDI 52)
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.375),
    # Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=50, start=4.375, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 (Bar 3: Bb7, Bar 4: Cm7)
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    # Hi-hats
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Continue the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=56, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line continuing
bass_notes = [
    # C (MIDI 52)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),
    # Bb (MIDI 50) chromatic approach from B (MIDI 51)
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=50, start=5.125, end=5.5),
    # F (MIDI 48)
    pretty_midi.Note(velocity=100, pitch=48, start=5.5, end=5.875),
    # C (MIDI 52)
    pretty_midi.Note(velocity=100, pitch=52, start=5.875, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 (Bar 4: Cm7)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
