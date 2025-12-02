
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D, F#, A, B, D, F#, A, B) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F natural (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # F natural (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F#
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# D7 = D F# A C
# G7 = G B D F
# A7 = A C# E G
# B7 = B D# F# A
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75), # A
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.75), # F#
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.75), # C

    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5), # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5), # B
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5), # F

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.25), # A
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25), # C#
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25), # E
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25), # G

    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0), # B
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0), # D#
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0), # F#
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.0), # A

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.75), # F#
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.75), # C

    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5), # B
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.5), # F
]

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 6):
    # Kick on 1 and 3
    start = i * 1.5 + 0.0
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))
    start = i * 1.5 + 1.125
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))

    # Snare on 2 and 4
    start = i * 1.5 + 0.75
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))
    start = i * 1.5 + 1.875
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))

    # Hi-hat on every eighth
    for j in range(0, 4):
        start = i * 1.5 + j * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Dante: Tenor sax melody (start at bar 2)
# Short motif: D (62), F# (65), B (69), C (60)
# Start at 1.5s, leave it hanging at 2.25s, then come back at 4.5s

# First phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B
]

# Second phrase (return at 4.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75))  # C
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25))  # F#
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # B

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
