
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with roots and fifths, chromatic approaches
bass_notes = []
bar_start = 1.5
for bar in range(2, 5):
    time = bar_start + (bar - 2) * 1.5
    if bar == 2:
        # Dm7
        notes = [D2, F2, A2, C3]
        chromatic = [D2, D2 - 1, D2 + 1]
        for i, note in enumerate(notes):
            start = time + i * 0.375
            end = start + 0.375
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))
        # Chromatic approach on 3
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[1], start=time + 0.75, end=time + 0.75 + 0.125))
    elif bar == 3:
        # G7
        notes = [G2, B2, D3, F3]
        chromatic = [G2, G2 - 1, G2 + 1]
        for i, note in enumerate(notes):
            start = time + i * 0.375
            end = start + 0.375
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))
        # Chromatic approach on 3
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[1], start=time + 0.75, end=time + 0.75 + 0.125))
    elif bar == 4:
        # Cmaj7
        notes = [C2, E2, G2, B2]
        chromatic = [C2, C2 - 1, C2 + 1]
        for i, note in enumerate(notes):
            start = time + i * 0.375
            end = start + 0.375
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))
        # Chromatic approach on 3
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[1], start=time + 0.75, end=time + 0.75 + 0.125))

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on last bar
piano_notes = []
for bar in range(2, 5):
    time = bar_start + (bar - 2) * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.75))
    elif bar == 3:
        # G7: G, B, D, F
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time, end=time + 0.75))
    elif bar == 4:
        # Cmaj7: C, E, G, B
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.75))
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.75))
        # Resolve on last bar
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time + 0.75, end=time + 1.5))

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, sing it, leave it hanging, come back and finish
# Motif: D, E, F#, D
sax_notes = []
time = bar_start
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 0.75, end=time + 1.125))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 1.125, end=time + 1.5))
# Come back and finish on 4th bar
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 3.0, end=time + 3.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + 3.375, end=time + 3.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time + 3.75, end=time + 4.125))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 4.125, end=time + 4.5))

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
