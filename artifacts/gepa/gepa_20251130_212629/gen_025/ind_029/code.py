
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]
instrument_programs = {
    'drums': pretty_midi.instrument_name_to_program('Acoustic Drums'),
    'bass': pretty_midi.instrument_name_to_program('Double Bass'),
    'piano': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'sax': pretty_midi.instrument_name_to_program('Tenor Saxophone'),
}

# Create instruments
drums = pretty_midi.Instrument(program=instrument_programs['drums'])
bass = pretty_midi.Instrument(program=instrument_programs['bass'])
piano = pretty_midi.Instrument(program=instrument_programs['piano'])
sax = pretty_midi.Instrument(program=instrument_programs['sax'])

# BPM: 160 => beat duration in seconds = 60 / 160 = 0.375
beat = 0.375
bar = beat * 4  # 1.5s

# Set up time
time = 0.0

# --------------------
# BAR 1: Little Ray (drums) — just hihat for tension
# --------------------
# Hihat on every eighth, but with subtle dynamic variation (velocity from 40-80)
for i in range(8):
    note_number = 60  # C4 for hihat
    note_time = time + i * beat / 2
    note = pretty_midi.Note(
        velocity=np.random.randint(40, 80),
        pitch=note_number,
        start=note_time,
        end=note_time + beat / 2 - 0.01
    )
    drums.notes.append(note)

time += bar

# --------------------
# BAR 2: Marcus (bass) — walking line with chromatic passing tones
# --------------------
# F major: F, G, A, Bb, C, D, E, F
# Walk: F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
# Use chromatic passing tones for tension
bass_notes = [77, 76, 78, 77, 79, 78, 80, 79, 81, 80, 82, 81]  # F, Gb, G, Ab, A, Bb, B, C, D, Eb, E, F
for note in bass_notes:
    note_duration = beat / 4  # 16th note
    note_start = time + (bass_notes.index(note) % 4) * note_duration
    note = pretty_midi.Note(
        velocity=60,
        pitch=note,
        start=note_start,
        end=note_start + note_duration
    )
    bass.notes.append(note)

# Add a subtle dynamic shift in the last two notes
bass.notes[-2].velocity = 65
bass.notes[-1].velocity = 63

time += bar

# --------------------
# BAR 3: Diane (piano) — 7th chords on 2 and 4, with comping
# --------------------
# F7 (F, A, C, E), Bb7 (Bb, D, F, Ab)
# Play on 2 and 4 (beat 2 and 4 of the bar)
chord1 = [76, 79, 81, 84]  # F7
chord2 = [74, 77, 79, 81]  # Bb7

# Play on beat 2 and 4
for i, chord in enumerate([chord1, chord2]):
    for note in chord:
        note_start = time + (i + 1) * beat  # beat 2 and 4
        note_duration = beat / 2
        note = pretty_midi.Note(
            velocity=75 + np.random.randint(-5, 5),
            pitch=note,
            start=note_start,
            end=note_start + note_duration
        )
        piano.notes.append(note)

time += bar

# --------------------
# BAR 4: You (sax) — the motif
# --------------------
# Tenor sax: Start with a motif, leave it hanging
# Notes: F, Bb, C, Eb (F7) — but with a slight delay on the last note
motif = [77, 74, 81, 84]
start_times = [time, time + beat*0.25, time + beat*0.5, time + beat*0.75]
for i, note in enumerate(motif):
    duration = beat * 0.25
    if i == 3:
        # End on the last note, leave it hanging
        duration = beat * 0.75
    note = pretty_midi.Note(
        velocity=85,
        pitch=note,
        start=start_times[i],
        end=start_times[i] + duration
    )
    sax.notes.append(note)

# Add a slight dynamic drop on the last note
sax.notes[-1].velocity = 75

# Add the instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("jazz_intro.mid")
