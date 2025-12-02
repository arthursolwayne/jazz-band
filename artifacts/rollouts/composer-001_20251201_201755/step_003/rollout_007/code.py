
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

# Bass: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (F7 - D2, G2, chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25), # C2 chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25), # D2

    # Bar 3 (Bb7 - D2, A2, chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0), # G2 chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # D2

    # Bar 4 (F7 - D2, G2, chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75), # C2 chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, different chord each bar, resolve on last)
# Bar 2: F7 - F, A, C, E
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # E

    # Bar 3: Bb7 - Bb, D, F, A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # A

    # Bar 4: F7 - F, A, C, E
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375), # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: F, Bb, C, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.375), # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75), # F (leaving it hanging)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F (come back and finish it)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4

    # Bar 3 (Fill)
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=6.25, end=6.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=6.25, end=6.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.625, end=7.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.625, end=7.0),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
