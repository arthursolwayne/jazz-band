
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Setup the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Dm in MIDI (D=62, F=64, Ab=67)
D = 62
F = 64
Ab = 67

# Define time for each bar (6 seconds for 4 bars)
BAR_DURATION = 1.5  # seconds per bar at 160 BPM (60/160 * 4 = 1.5)
BAR_RESOLUTION = 480  # MIDI ticks per bar

# Define the note durations and timing for each instrument

# 1. Drums (Little Ray)
drums = Instrument(program=Program.DRUMS)
drums.is_drum = True

# Kick on 1 and 3
for bar in range(4):
    kick_time = bar * BAR_DURATION + 0.0  # beat 1
    kick = Note(36, 100, kick_time, kick_time + 0.1)
    drums.notes.append(kick)

    kick_time = bar * BAR_DURATION + 0.75  # beat 3
    kick = Note(36, 100, kick_time, kick_time + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4
for bar in range(4):
    snare_time = bar * BAR_DURATION + 0.375  # beat 2
    snare = Note(38, 100, snare_time, snare_time + 0.1)
    drums.notes.append(snare)

    snare_time = bar * BAR_DURATION + 1.125  # beat 4
    snare = Note(38, 100, snare_time, snare_time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(8):
        hihat_time = bar * BAR_DURATION + (i * 0.1875)
        hihat = Note(42, 80, hihat_time, hihat_time + 0.05)
        drums.notes.append(hihat)

# 2. Bass (Marcus)
bass = Instrument(program=Program.BASS)

# Walking line: chromatic approach to Dm
# This is a unique pattern that avoids repetition
bass_notes = [
    D - 1,  # C# (chromatic approach)
    D,
    F,
    Ab,
    D,
    F,
    Ab - 1,  # G#
    Ab,
    D,
    F,
    Ab,
    D,
    F,
    D - 1,  # C#
    F,
    Ab
]

for i, note in enumerate(bass_notes):
    time = (i / 8) * BAR_DURATION  # 8 notes per bar
    duration = BAR_DURATION / 8
    bass_note = Note(note, 80, time, time + duration)
    bass.notes.append(bass_note)

# 3. Piano (Diane)
piano = Instrument(program=Program.PIANO)

# 7th chords: Dm7 = D F Ab C
# Comping on 2 and 4
for bar in range(4):
    # Comp on 2
    time = bar * BAR_DURATION + 0.375
    chord = [D, F, Ab, 60]  # C
    for n in chord:
        piano_note = Note(n, 80, time, time + 0.2)
        piano.notes.append(piano_note)

    # Comp on 4
    time = bar * BAR_DURATION + 1.125
    for n in chord:
        piano_note = Note(n, 80, time, time + 0.2)
        piano.notes.append(piano_note)

# 4. Tenor Sax (You)
sax = Instrument(program=Program.SAXOPHONE)

# One short motif: start strong, leave it hanging, resolve later
# Dm motif: D -> F -> Ab -> D (with space and dynamics)
sax_notes = [
    Note(D, 110, 0.0, 0.2),
    Note(F, 110, 0.5, 0.2),
    Note(Ab, 110, 0.75, 0.2),
    Note(D, 110, 1.375, 0.2)
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Save to file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
