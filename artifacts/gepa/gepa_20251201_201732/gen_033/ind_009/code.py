
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
drum_notes = []
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = []
bass_root = pretty_midi.note_number_to_name(38)  # D2
bass_fifth = pretty_midi.note_number_to_name(43)  # G2

for bar in range(2, 5):  # Bars 2, 3, 4
    start_time = (bar - 1) * 1.5
    # Root (D2)
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start_time, end=start_time + 0.375))
    # Chromatic approach to fifth (G2)
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.75))
    # Fifth (G2)
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=start_time + 0.75, end=start_time + 1.125))
    # Chromatic approach to root (D2)
    bass_notes.append(pretty_midi.Note(velocity=80, pitch=37, start=start_time + 1.125, end=start_time + 1.5))
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []

# Bar 2: Dm7 (D, F, A, C)
for note in [38, 41, 45, 48]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.5 + 0.75))

# Bar 3: G7 (G, B, D, F)
for note in [43, 47, 50, 53]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.0 + 0.75))

# Bar 4: Cm7 (C, Eb, G, Bb)
for note in [48, 50, 55, 57]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.5 + 0.75))

piano.notes.extend(piano_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    for beat in [0, 1, 2, 3]:
        time = start_time + beat * 0.375
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        # Hi-hat on every eighth
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D, F#, C, D
sax_notes = []
bar_start = 1.5
note_durations = [0.375, 0.375, 0.375, 0.375]

# Bar 2: Start motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start, end=bar_start + note_durations[0]))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=bar_start + note_durations[0], end=bar_start + note_durations[0] + note_durations[1]))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=32, start=bar_start + note_durations[0] + note_durations[1], end=bar_start + note_durations[0] + note_durations[1] + note_durations[2]))

# Bar 3: Leave the motif hanging, then finish it
sax_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.0 + note_durations[3]))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
