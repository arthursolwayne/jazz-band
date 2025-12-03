
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
            drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
bar_start = 1.5
for bar in range(3):
    for beat in range(4):
        time = bar_start + beat * 0.375
        root = 50  # D2
        if beat == 0:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=root, start=time, end=time + 0.375))
        elif beat == 1:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=root + 7, start=time, end=time + 0.375))  # G2
        elif beat == 2:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=root + 1, start=time, end=time + 0.375))  # D#2
        elif beat == 3:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=root + 7, start=time, end=time + 0.375))  # G2

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = []
chords = [
    [(60, 64, 67, 72), (64, 67, 72, 76)],  # Dm7 (60, 64, 67, 72) -> G7 (64, 67, 72, 76)
    [(62, 66, 69, 74), (66, 69, 74, 78)],  # Em7 (62, 66, 69, 74) -> A7 (66, 69, 74, 78)
    [(60, 64, 67, 72), (64, 67, 72, 76)],  # Dm7 (60, 64, 67, 72) -> G7 (64, 67, 72, 76)
]
for bar in range(3):
    bar_start_time = 1.5 + bar * 1.5
    for beat in range(2):  # Comp on 2 and 4
        time = bar_start_time + beat * 0.75
        chord = chords[bar]
        for note in chord:
            piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

piano.notes.extend(piano_notes)

# You: Tenor sax, short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar_start_time = 1.5
# Bar 2: Start the motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_start_time, end=bar_start_time + 0.375))  # E4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_start_time + 0.375, end=bar_start_time + 0.75))  # G4
# Bar 3: Let it hang
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_start_time + 1.5, end=bar_start_time + 1.875))  # E4
# Bar 4: Finish the motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_start_time + 3.0, end=bar_start_time + 3.375))  # G4

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
