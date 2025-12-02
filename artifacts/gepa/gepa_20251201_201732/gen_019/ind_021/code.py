
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
pm.instruments.append(instrument)

# Tempo and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160.0, time=0.0)]

# Define the time per bar
BPM = 160
beats_per_bar = 4
time_per_beat = 60.0 / BPM
time_per_bar = time_per_beat * beats_per_bar

# Define the timeline for each bar
bar_start_times = [0, time_per_bar, time_per_bar * 2, time_per_bar * 3]

# BAR 1: Little Ray - Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    bar_time = bar_start_times[bar]
    for beat in range(4):
        time = bar_time + beat * time_per_beat
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(
                velocity=80,
                pitch=36,  # Kick
                start=time,
                end=time + 0.1
            )
            instrument.notes.append(note)
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(
                velocity=90,
                pitch=38,  # Snare
                start=time,
                end=time + 0.1
            )
            instrument.notes.append(note)
        # Hihat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(
                velocity=60,
                pitch=46,  # Hihat
                start=time + eighth * time_per_beat / 2,
                end=time + eighth * time_per_beat / 2 + 0.05
            )
            instrument.notes.append(note)

# BAR 2: Diane on piano - Open voicings, different chords each bar, resolve on the last
# Chord progression: Dmaj7 -> Bm7 -> F#m7 -> A7
chords = {
    0: [62, 67, 72, 76],  # Dmaj7 (D, F#, A, C#)
    1: [65, 70, 75, 79],  # Bm7 (B, D, F#, A)
    2: [67, 72, 77, 80],  # F#m7 (F#, A, C#, E)
    3: [69, 74, 79, 82]   # A7 (A, C#, E, G#)
}

for bar in range(2, 4):
    bar_time = bar_start_times[bar]
    for chord_idx, chord in enumerate(chords[bar - 2]):
        time = bar_time + (chord_idx * time_per_beat) + 0.25  # Comp on 2 and 4
        if (chord_idx == 1 or chord_idx == 3):  # Comp on 2 and 4
            note = pretty_midi.Note(
                velocity=100,
                pitch=chord,
                start=time,
                end=time + 0.1
            )
            instrument.notes.append(note)

# BAR 2-4: Marcus on bass - Walking line, roots and fifths with chromatic approaches
# D2-G2, MIDI 38-43 (D2 = 38, G2 = 43)
# Root on 1, fifth on 3, chromatic approach on 2 and 4
bass_line = [38, 40, 43, 41]  # D2, F2, G2, F#2
# Repeat for each bar
for bar in range(2, 4):
    bar_time = bar_start_times[bar]
    for beat, note in enumerate(bass_line):
        time = bar_time + beat * time_per_beat
        if beat == 0 or beat == 2:  # Root and fifth
            note_obj = pretty_midi.Note(
                velocity=70,
                pitch=note,
                start=time,
                end=time + 0.1
            )
            instrument.notes.append(note_obj)

# BAR 2-4: You on tenor sax - Motif, start it, leave it hanging, come back and finish
# Motif: D4 (62), F#4 (67), A4 (72), D5 (72), D4 (62)
# Start on beat 1, rest on 2, play 3 and 4
motif = [62, 67, 72, 72, 62]  # D4, F#4, A4, A4, D4
time = bar_start_times[2]  # Bar 2

# Play first note on beat 1
note = pretty_midi.Note(
    velocity=100,
    pitch=motif[0],
    start=time,
    end=time + 0.25
)
instrument.notes.append(note)

# Rest on beat 2
# Play 3 and 4
for i in range(1, len(motif)):
    time_i = time + (i * time_per_beat)
    note = pretty_midi.Note(
        velocity=100,
        pitch=motif[i],
        start=time_i,
        end=time_i + 0.1
    )
    instrument.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro_wayne.mid")
print("MIDI file created: jazz_intro_wayne.mid")
