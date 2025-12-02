
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
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif: start with a short phrase, leave it hanging

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D (Dm7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G (Dm7)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A (Dm7)
]

# Bar 3
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # G (Dm7)
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D (Dm7)
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # C (Dm7)
])

# Bar 4
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # Eb (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D (Dm7)
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # G (Dm7)
])

# Bar 5
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # A (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # G (Dm7)
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # Eb (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D (Dm7)
])

# Bar 6
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F (Dm7)
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # G (Dm7)
])

sax.notes.extend(sax_notes)

# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # F

    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # D

    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=4.25, end=4.5),  # G

    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # F

    pretty_midi.Note(velocity=80, pitch=53, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=5.75, end=6.0),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(2, 6):
    if bar % 2 == 0:
        # Comp on 2 and 4
        for beat in [1, 3]:
            time = bar * 1.5 + beat * 0.375
            # Dm7: D, F, A, C
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.25))
            piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.25))

piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 6):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
