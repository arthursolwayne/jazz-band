
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define tempo in MIDI units (BPM = 160, so 60 / 160 = 0.375 seconds per beat)
# Use this for timing calculations
beat_time = 60.0 / 160  # 0.375 seconds per beat
bar_time = beat_time * 4  # 1.5 seconds per bar

# Define note functions
def note_on(note, time, duration, velocity=100):
    return Note(note, time, duration, velocity)

# Drums (Program 0)
drum_program = Program(0)
drum_instrument = Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Bar 1: Little Ray (drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0
for beat in [0, 2]:  # 1 and 3
    kick = note_on(36, bar1_start + beat * beat_time, beat_time / 2, 100)
    drum_instrument.notes.append(kick)

for beat in [1, 3]:  # 2 and 4
    snare = note_on(38, bar1_start + beat * beat_time, beat_time / 2, 100)
    drum_instrument.notes.append(snare)

for beat in range(4):
    hihat = note_on(42, bar1_start + beat * beat_time + beat_time / 2, beat_time / 2, 90)
    drum_instrument.notes.append(hihat)

# Bass (Program 33 - Acoustic Bass)
bass_program = Program(33)
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Bar 2: Marcus (bass) - Walking line, chromatic approach
bar2_start = bar_time
# Fm7 -> E♭m7 -> Dm7 -> Cm7 (chromatic descending approach)
# Walking line: F, E♭, D, C, B♭, A, G, F (F to F)
notes = [71, 68, 67, 64, 62, 60, 59, 57]  # F, E♭, D, C, B♭, A, G, F
for i, note in enumerate(notes):
    duration = beat_time / 2  # Half note
    start = bar2_start + i * beat_time
    bass_note = note_on(note, start, duration, 80)
    bass_instrument.notes.append(bass_note)

# Piano (Program 0 - Acoustic Grand Piano)
piano_program = Program(0)
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Bar 2: Diane (piano) - 7th chords on 2 and 4
bar2_start = bar_time
# Fm7: F, Ab, C, Eb
# Bm7: B, D, F#, A
# Cm7: C, Eb, G, Bb
# Gm7: G, Bb, D, F
chords = [
    [71, 68, 64, 62],  # Fm7
    [73, 68, 67, 62],  # Bm7
    [72, 62, 67, 64],  # Cm7
    [76, 68, 71, 67],  # Gm7
]
for i, chord in enumerate(chords):
    if i in [1, 3]:  # 2 and 4
        for note in chord:
            start = bar2_start + i * beat_time
            duration = beat_time / 2
            piano_note = note_on(note, start, duration, 80)
            piano_instrument.notes.append(piano_note)

# Tenor Sax (Program 62 - Tenor Sax)
sax_program = Program(62)
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Bar 2–4: Dante (tenor sax) - Melody
bar2_start = bar_time
# Melody motif: F, D, B♭, F (Fm with chromatic underpinning)
# Start with F, D, B♭, leave it hanging on B♭, resolve to F in bar 4
notes = [
    # Bar 2: F, D, Bb
    [71, 68, 62],
    # Bar 3: D, F, Bb (chromatic run)
    [68, 71, 62],
    # Bar 4: D, F, F (resolve)
    [68, 71, 71]
]

for i, bar_notes in enumerate(notes):
    for j, note in enumerate(bar_notes):
        start = bar2_start + i * beat_time + j * beat_time
        duration = beat_time / 2
        sax_note = note_on(note, start, duration, 100)
        sax_instrument.notes.append(sax_note)

# Save the MIDI file
pm.write('dante_intro.mid')

print("MIDI file created: 'dante_intro.mid'")
