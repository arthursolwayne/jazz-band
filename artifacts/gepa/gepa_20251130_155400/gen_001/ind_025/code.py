
import pretty_midi
import numpy as np

# Constants
BPM = 160
BEATS_PER_BAR = 4
SECONDS_PER_BAR = 6.0 / BEATS_PER_BAR  # 1.5 seconds per bar
SAMPLE_RATE = 44100
TIME_SIGNATURE = (4, 4)
KEY = 'Dm'  # D minor

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Time conversion functions
def beat_to_seconds(beat):
    return (beat / BPM) * 60.0

def bar_to_seconds(bar):
    return beat_to_seconds(bar * BEATS_PER_BAR)

# Add instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program, is_drum=True)

pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# ===================
# BAR 1: DRUMS ONLY (setup)
# ===================
# Kick on 1 and 3
drum_notes = [
    (pretty_midi.note_name_to_number('C1'), 0.0),  # Kick on beat 1
    (pretty_midi.note_name_to_number('C1'), 1.5),  # Kick on beat 3
]

# Snare on 2 and 4
drum_notes.append((pretty_midi.note_name_to_number('Snare'), 0.75))
drum_notes.append((pretty_midi.note_name_to_number('Snare'), 2.25))

# Hi-hat on every eighth
for i in range(8):
    time = i * 0.375
    drum_notes.append((pretty_midi.note_name_to_number('Closed Hi-Hat'), time))

for note, time in drum_notes:
    note_obj = pretty_midi.Note(
        velocity=100, pitch=note, start=time, end=time + 0.125
    )
    drums.notes.append(note_obj)

# ===================
# BAR 2-4: FULL BAND
# ===================
# Time for Bar 2
bar_2_start = bar_to_seconds(1)

# SAX: Melodic motif in Dm with emotional weight
# Dm = D, F, A, C
# Motif: D - F - C - F (staccato, then legato on F)
sax_notes = [
    (pretty_midi.note_name_to_number('D4'), bar_2_start + 0.0, 0.25),  # D4
    (pretty_midi.note_name_to_number('F4'), bar_2_start + 0.25, 0.125),  # F4
    (pretty_midi.note_name_to_number('C4'), bar_2_start + 0.375, 0.25),  # C4
    (pretty_midi.note_name_to_number('F4'), bar_2_start + 0.625, 0.25),  # F4
]

for pitch, start, duration in sax_notes:
    note_obj = pretty_midi.Note(
        velocity=110, pitch=pitch, start=start, end=start + duration
    )
    sax.notes.append(note_obj)

# BASS: Walking line, chromatic, no repeated notes
# Start on D (root of Dm), walk down chromatically
# D -> C -> Bb -> A -> G -> F -> Eb -> D -> C -> B -> A -> G -> F -> Eb -> D
bass_notes = [
    (pretty_midi.note_name_to_number('D2'), bar_2_start + 0.0, 0.25),     # D2
    (pretty_midi.note_name_to_number('C2'), bar_2_start + 0.25, 0.25),   # C2
    (pretty_midi.note_name_to_number('Bb2'), bar_2_start + 0.5, 0.25),  # Bb2
    (pretty_midi.note_name_to_number('A2'), bar_2_start + 0.75, 0.25),   # A2
    (pretty_midi.note_name_to_number('G2'), bar_2_start + 1.0, 0.25),    # G2
    (pretty_midi.note_name_to_number('F2'), bar_2_start + 1.25, 0.25),   # F2
    (pretty_midi.note_name_to_number('Eb2'), bar_2_start + 1.5, 0.25),   # Eb2
    (pretty_midi.note_name_to_number('D2'), bar_2_start + 1.75, 0.25),   # D2
    (pretty_midi.note_name_to_number('C2'), bar_2_start + 2.0, 0.25),    # C2
    (pretty_midi.note_name_to_number('B2'), bar_2_start + 2.25, 0.25),   # B2
    (pretty_midi.note_name_to_number('A2'), bar_2_start + 2.5, 0.25),    # A2
    (pretty_midi.note_name_to_number('G2'), bar_2_start + 2.75, 0.25),   # G2
    (pretty_midi.note_name_to_number('F2'), bar_2_start + 3.0, 0.25),    # F2
    (pretty_midi.note_name_to_number('Eb2'), bar_2_start + 3.25, 0.25),  # Eb2
    (pretty_midi.note_name_to_number('D2'), bar_2_start + 3.5, 0.25),    # D2
]

for pitch, start, duration in bass_notes:
    note_obj = pretty_midi.Note(
        velocity=70, pitch=pitch, start=start, end=start + duration
    )
    bass.notes.append(note_obj)

# PIANO: 7th chords on beats 2 and 4
# Dm7 = D, F, A, C
# Comp on beats 2 and 4 in each bar
piano_notes = []
for bar in [1, 2, 3]:  # Bars 2-4 (indices 1-3 since bar 1 is setup)
    bar_start = bar_to_seconds(bar)
    # Beat 2: Dm7 on beat 2
    for pitch in [pretty_midi.note_name_to_number('D3'), pretty_midi.note_name_to_number('F3'),
                  pretty_midi.note_name_to_number('A3'), pretty_midi.note_name_to_number('C3')]:
        note_obj = pretty_midi.Note(
            velocity=80, pitch=pitch, start=bar_start + 0.75, end=bar_start + 0.75 + 0.25
        )
        piano.notes.append(note_obj)
    
    # Beat 4: Dm7 on beat 4
    for pitch in [pretty_midi.note_name_to_number('D3'), pretty_midi.note_name_to_number('F3'),
                  pretty_midi.note_name_to_number('A3'), pretty_midi.note_name_to_number('C3')]:
        note_obj = pretty_midi.Note(
            velocity=80, pitch=pitch, start=bar_start + 2.25, end=bar_start + 2.25 + 0.25
        )
        piano.notes.append(note_obj)

# Save the MIDI file
pm.time_signature_changes = [pretty_midi.TimeSignature(*TIME_SIGNATURE, bar_to_seconds(0))]
pm.write('dante_russo_intro.mid')
