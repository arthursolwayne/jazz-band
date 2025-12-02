
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define key: F minor
key = 'Fm'

# Bar length in seconds
bar_length = 1.5

# Define the four bars
bars = 4

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drum_program = pretty_midi.instrument_name_to_program('Drums')

# Add instruments
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)
drum_instrument = pretty_midi.Instrument(program=drum_program)

pm.instruments.extend([bass_instrument, piano_instrument, sax_instrument, drum_instrument])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drum_pattern(instrument, start_time, bar_length, tempo=160):
    beats_per_bar = 4
    beats_per_second = tempo / 60
    beat_duration = 1 / beats_per_second
    eighth_note = beat_duration / 2
    times = []
    for bar in range(bars):
        for beat in range(beats_per_bar):
            time = start_time + bar * bar_length + beat * beat_duration
            # Kick on 1 and 3
            if beat == 0 or beat == 2:
                instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
            # Snare on 2 and 4
            if beat == 1 or beat == 3:
                instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
            # Hihat on every eighth
            for i in range(2):
                instrument.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=time + i * eighth_note, end=time + i * eighth_note + 0.05))
    return

# Bass line: Walking line in Fm, roots and fifths with chromatic approaches
def add_bass_line(instrument, start_time, bar_length, tempo=160):
    # Fm scale degrees: F, Gb, Ab, A, Bb, C, Db
    # Root: F (70), 5th: C (60), chromatic approach up/down
    notes = [
        # Bar 1: F -> Gb -> C -> F
        (70, 0.0), (60, 0.25), (61, 0.5), (70, 0.75),
        # Bar 2: Ab -> A -> Bb -> C
        (69, 1.0), (71, 1.25), (72, 1.5), (60, 1.75),
        # Bar 3: Db -> C -> F -> Gb
        (64, 2.0), (60, 2.25), (70, 2.5), (60, 2.75),
        # Bar 4: F -> Ab -> C -> F
        (70, 3.0), (69, 3.25), (60, 3.5), (70, 3.75),
    ]
    for pitch, time_offset in notes:
        start = start_time + time_offset
        end = start + 0.25
        instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))
    return

# Piano: Open voicings, resolving on the last beat of each bar
def add_piano_chords(instrument, start_time, bar_length, tempo=160):
    # Chords: Fm7, Ab7, Bb7, C7 (each bar)
    # Fm7: F, Ab, C, Eb (70, 69, 60, 62)
    # Ab7: Ab, C, Eb, Gb (69, 60, 62, 60)
    # Bb7: Bb, D, F, Ab (72, 64, 70, 69)
    # C7: C, E, G, Bb (60, 64, 67, 72)
    chords = [
        [70, 69, 60, 62],
        [69, 60, 62, 60],
        [72, 64, 70, 69],
        [60, 64, 67, 72],
    ]
    for bar_idx, chord in enumerate(chords):
        start = start_time + bar_idx * bar_length
        # Play chord on beat 2 and 4
        for beat in [1, 3]:
            time = start + beat * (bar_length / 4)
            for pitch in chord:
                instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.1))
    return

# Tenor Sax: A short motif — one phrase that hangs and returns
def add_tenor_sax(instrument, start_time, bar_length, tempo=160):
    # Motif: F (70) -> Ab (69) -> C (60) -> F (70)
    # Play it on beat 1 and 3 of bar 1 and 2
    # First phrase: beat 1
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=70, start=start_time, end=start_time + 0.3))
    # Second note: beat 1 + 0.3
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=69, start=start_time + 0.3, end=start_time + 0.6))
    # Third note: beat 1 + 0.6
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=start_time + 0.6, end=start_time + 0.9))
    # Let it hang — silence for beat 2
    # Now repeat on beat 3
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=70, start=start_time + 1.5, end=start_time + 1.8))
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=69, start=start_time + 1.8, end=start_time + 2.1))
    instrument.notes.append(pretty_midi.Note(velocity=105, pitch=60, start=start_time + 2.1, end=start_time + 2.4))
    return

# Add all parts
add_drum_pattern(drum_instrument, 0, bar_length)
add_bass_line(bass_instrument, 0, bar_length)
add_piano_chords(piano_instrument, 0, bar_length)
add_tenor_sax(sax_instrument, 0, bar_length)

# Save the MIDI
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been generated.")
