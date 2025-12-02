
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with the tempo
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Bass
piano = pretty_midi.NoteSequenceInstrument(program=0)  # Piano
sax = pretty_midi.Instrument(program=64)    # Tenor sax

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Time per beat in seconds
beat_time = 60.0 / 160.0  # 0.375s per beat

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in [0, 2]:  # Beats 1 and 3
        kick_time = bar * 4 * beat_time + beat * beat_time
        kick_velocity = np.random.randint(80, 100)
        kick = pretty_midi.Note(name='C2', start=kick_time, end=kick_time + 0.1, velocity=kick_velocity)
        drums.notes.append(kick)

    for beat in [1, 3]:  # Beats 2 and 4
        snare_time = bar * 4 * beat_time + beat * beat_time
        snare_velocity = np.random.randint(80, 100)
        snare = pretty_midi.Note(name='C3', start=snare_time, end=snare_time + 0.1, velocity=snare_velocity)
        drums.notes.append(snare)

    for eighth in range(8):  # Every eighth note
        hihat_time = bar * 4 * beat_time + (eighth * beat_time / 2)
        hihat_velocity = np.random.randint(50, 70)
        hihat = pretty_midi.Note(name='C6', start=hihat_time, end=hihat_time + 0.05, velocity=hihat_velocity)
        drums.notes.append(hihat)

# Bars 2-4: All instruments in
# Time for bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 4 * beat_time

    # Bass: Walking line with chromatic passing tones
    # We'll use a simple D minor 7th scale with chromaticism for passing
    bass_notes = [
        'C#2', 'D2', 'E2', 'F2',  # Bar 2
        'F#2', 'G2', 'A2', 'Bb2', # Bar 3
        'B2', 'C2', 'C#2', 'D2'   # Bar 4
    ]

    for i, note in enumerate(bass_notes):
        start_time = bar_start + (i * beat_time / 4)
        end_time = start_time + 0.25
        velocity = np.random.randint(60, 80)
        bass_note = pretty_midi.Note(name=note, start=start_time, end=end_time, velocity=velocity)
        bass.notes.append(bass_note)

    # Piano: 7th chords on beats 2 and 4
    # Dm7 = D, F, A, C
    # D7 = D, F#, A, C
    # Dm7 = D, F, A, C
    # D7 = D, F#, A, C
    # Alternating between Dm7 and D7

    if bar == 2 or bar == 4:
        # Dm7 on beat 2
        start_time = bar_start + beat_time * 1
        chord = ['F3', 'A3', 'C4', 'D4']
        for note in chord:
            piano_note = pretty_midi.Note(name=note, start=start_time, end=start_time + 0.1, velocity=60)
            piano.notes.append(piano_note)

        # Dm7 on beat 4
        start_time = bar_start + beat_time * 3
        for note in chord:
            piano_note = pretty_midi.Note(name=note, start=start_time, end=start_time + 0.1, velocity=60)
            piano.notes.append(piano_note)
    else:
        # D7 on beat 2
        start_time = bar_start + beat_time * 1
        chord = ['F#3', 'A3', 'C4', 'D4']
        for note in chord:
            piano_note = pretty_midi.Note(name=note, start=start_time, end=start_time + 0.1, velocity=60)
            piano.notes.append(piano_note)

        # D7 on beat 4
        start_time = bar_start + beat_time * 3
        for note in chord:
            piano_note = pretty_midi.Note(name=note, start=start_time, end=start_time + 0.1, velocity=60)
            piano.notes.append(piano_note)

    # Sax: Melody - concise, expressive, memorable
    # Melody: D, F#, Bb, C
    # Start on beat 1 of bar 2
    if bar == 2:
        melody_notes = [
            ('D4', 0.0),    # Start on beat 1
            ('F#4', 0.5),   # Beat 2 (half note)
            ('Bb4', 0.5),   # Beat 3
            ('C5', 0.5)     # Beat 4
        ]

        for i, (note, duration) in enumerate(melody_notes):
            start_time = bar_start + i * beat_time
            end_time = start_time + duration
            velocity = 100
            sax_note = pretty_midi.Note(name=note, start=start_time, end=end_time, velocity=velocity)
            sax.notes.append(sax_note)

# Write the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been created.")
