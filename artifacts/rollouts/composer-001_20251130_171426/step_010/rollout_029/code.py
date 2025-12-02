
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.125))

# Sax (Dante) - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (66) - D (62) - Bb (62)
# Start with the first three notes, then come back with the full motif

# First pass (1.5 - 2.25s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875))

# Full motif pass (2.5 - 3.25s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
