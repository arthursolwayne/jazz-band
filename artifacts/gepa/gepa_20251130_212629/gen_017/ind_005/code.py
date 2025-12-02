
import pretty_midi

# Setup
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
pm.instruments.append(instrument)

# Tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0,螃蟹)]
pm.tempos = [pretty_midi.TempoChangeEvent(tempo=160.0, time=0.0)]

# Frequency conversion for note names
note_to_freq = {
    'F': 174.61,
    'G': 195.99,
    'Ab': 207.65,
    'Bb': 233.08,
    'C': 261.63,
    'Db': 277.18,
    'D': 293.66
}

# Define time per bar and beat
BPM = 160
time_per_beat = 60.0 / BPM  # seconds per beat
time_per_bar = 4 * time_per_beat  # 4/4 time
time_per_eighth = time_per_beat / 2

# Bar 1: Little Ray (drums)
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3

# Snare
snare = pretty_midi.Note(
    velocity=100,
    pitch=62,  # Snare drum (MIDI note 62)
    start=2.0 * time_per_beat,
    end=(2.0 + 0.1) * time_per_beat
)
snare2 = pretty_midi.Note(
    velocity=100,
    pitch=62,
    start=4.0 * time_per_beat,
    end=(4.0 + 0.1) * time_per_beat
)
instrument.notes.extend([snare, snare2])

# Kick
kick = pretty_midi.Note(
    velocity=110,
    pitch=36,  # Kick drum (MIDI note 36)
    start=1.0 * time_per_beat,
    end=(1.0 + 0.1) * time_per_beat
)
kick2 = pretty_midi.Note(
    velocity=110,
    pitch=36,
    start=3.0 * time_per_beat,
    end=(3.0 + 0.1) * time_per_beat
)
instrument.notes.extend([kick, kick2])

# Hihat on every eighth
hihat_note = pretty_midi.Note(
    velocity=100,
    pitch=42,  # Hihat (MIDI note 42)
    start=1.0 * time_per_beat,
    end=(1.0 + 0.05) * time_per_beat
)
for i in range(1, 9):
    hihat = pretty_midi.Note(
        velocity=100,
        pitch=42,
        start=i * time_per_eighth,
        end=(i * time_per_eighth) + 0.05
    )
    instrument.notes.append(hihat)

# Bars 2-4: Ensemble

# Marcus - Walking bass line in Fm
# Fm7: F, Ab, Bb, D
# Bbm7: Bb, Db, F, Ab
# Eb7: Eb, G, Bb, D
# Ab7: Ab, C, Eb, G

# Chromatic walking line:
# F -> G -> Ab -> Bb -> C -> Db -> D -> Eb -> F

note_times = [2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0]
notes = ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'D', 'Eb', 'F']

for time, note in zip(note_times, notes):
    note_num = pretty_midi.note_name_to_number(note)
    n = pretty_midi.Note(
        velocity=90,
        pitch=note_num,
        start=time,
        end=time + 0.25
    )
    instrument.notes.append(n)

# Diane - Piano comp on 2 and 4
# 7th chords: Fm7, Bbm7, Eb7, Ab7

# Fm7: F, Ab, Bb, D (Fm7 = F, Ab, Bb, D)
note_times_piano = [2.0, 4.0]
chords = [
    ['F', 'Ab', 'Bb', 'D'],
    ['Bb', 'Db', 'F', 'Ab'],
    ['Eb', 'G', 'Bb', 'D'],
    ['Ab', 'C', 'Eb', 'G']
]

for beat, chord in zip(note_times_piano, chords[0:2]):
    for note_name in chord:
        note_num = pretty_midi.note_name_to_number(note_name)
        n = pretty_midi.Note(
            velocity=90,
            pitch=note_num,
            start=beat,
            end=beat + 0.25
        )
        instrument.notes.append(n)

# Dante - Tenor sax: short motif
# Notes: F on "and" of 2, rest, then C on beat 3

# F on "and" of 2 = 2.25 seconds
note_f = pretty_midi.Note(
    velocity=100,
    pitch=pretty_midi.note_name_to_number('F'),
    start=2.25,
    end=2.25 + 0.125
)
instrument.notes.append(note_f)

# C on beat 3 (3.0)
note_c = pretty_midi.Note(
    velocity=100,
    pitch=pretty_midi.note_name_to_number('C'),
    start=3.0,
    end=3.0 + 0.125
)
instrument.notes.append(note_c)

# Save the MIDI
pm.save('jazz_intro_wayne.mid')
print("MIDI file generated: jazz_intro_wayne.mid")
