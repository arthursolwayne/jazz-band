
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet
# Marcus: Walking line in Fm (F, Ab, D, C, G, Bb, E, D)
# Diane: Open voicings, different chord each bar
# You: Short motif
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bass line (Bar 2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Bar 2)
piano_notes = [
    # F7/F6/F4 (open voicing)
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # F7
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # F6
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # F4

    # Ab7 (Bar 3)
    pretty_midi.Note(velocity=100, pitch=86, start=2.25, end=3.0),  # Ab7
    pretty_midi.Note(velocity=100, pitch=83, start=2.25, end=3.0),  # Ab6
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # Ab4

    # Dm7 (Bar 4)
    pretty_midi.Note(velocity=100, pitch=86, start=2.625, end=3.0),  # D7
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=3.0),  # D6
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Bar 2)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Saxophone (Bar 2-4)
# Short motif that sings, starts, leaves it hanging, returns
# Fm7 -> Ab7 -> Dm7 -> Fm7

sax_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # C

    # Bar 3 (Ab7)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C

    # Bar 4 (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
