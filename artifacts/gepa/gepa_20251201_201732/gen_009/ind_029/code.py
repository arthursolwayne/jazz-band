
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per beat (60 / BPM)
beat_time = 60.0 / 160

# Define the time for each bar
bar_time = 4 * beat_time  # 4/4 time

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_instr = Instrument(program=bass_program, is_drum=False)
pm.instruments.append(bass_instr)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano_instr = Instrument(program=piano_program, is_drum=False)
pm.instruments.append(piano_instr)

drum_program = pretty_midi.instrument_name_to_program('Drum Kit')
drum_instr = Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_instr)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instr = Instrument(program=sax_program, is_drum=False)
pm.instruments.append(sax_instr)

# Bass line: roots and fifths with chromatic approaches
bass_notes = [
    Note(38, 0, 0, 0.5),  # D2
    Note(44, 0, beat_time, 0.5),  # A2
    Note(43, 0, 2 * beat_time, 0.5),  # G2
    Note(47, 0, 3 * beat_time, 0.5),  # C3
    Note(48, 0, 4 * beat_time, 0.5),  # C#3
    Note(47, 0, 5 * beat_time, 0.5),  # C3
    Note(50, 0, 6 * beat_time, 0.5),  # E3
    Note(52, 0, 7 * beat_time, 0.5),  # G3
]

for note in bass_notes:
    bass_instr.notes.append(note)

# Piano chords: open voicings, different chord each bar, resolve on last
# Bar 1: D7 (no bass note)
piano_notes = [
    Note(55, 100, 0, 0.5),  # A3
    Note(62, 100, 0, 0.5),  # F#4
    Note(67, 100, 0, 0.5),  # C#5
    Note(64, 100, 0, 0.5),  # E4
]
for note in piano_notes:
    piano_instr.notes.append(note)

# Bar 2: Gm7
piano_notes = [
    Note(50, 100, 2 * beat_time, 0.5),  # E3
    Note(53, 100, 2 * beat_time, 0.5),  # G3
    Note(60, 100, 2 * beat_time, 0.5),  # D4
    Note(65, 100, 2 * beat_time, 0.5),  # Bb4
]
for note in piano_notes:
    piano_instr.notes.append(note)

# Bar 3: Cmaj7
piano_notes = [
    Note(52, 100, 4 * beat_time, 0.5),  # G3
    Note(57, 100, 4 * beat_time, 0.5),  # C4
    Note(64, 100, 4 * beat_time, 0.5),  # E4
    Note(69, 100, 4 * beat_time, 0.5),  # G4
]
for note in piano_notes:
    piano_instr.notes.append(note)

# Bar 4: F7
piano_notes = [
    Note(55, 100, 6 * beat_time, 0.5),  # A3
    Note(58, 100, 6 * beat_time, 0.5),  # C4
    Note(63, 100, 6 * beat_time, 0.5),  # Bb4
    Note(68, 100, 6 * beat_time, 0.5),  # D5
]
for note in piano_notes:
    piano_instr.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [
    Note(36, 100, 0, 0.3),
    Note(36, 100, 2 * beat_time, 0.3),
    Note(36, 100, 4 * beat_time, 0.3),
    Note(36, 100, 6 * beat_time, 0.3),
]
for note in kick_notes:
    drum_instr.notes.append(note)

snare_notes = [
    Note(38, 100, beat_time, 0.2),
    Note(38, 100, 3 * beat_time, 0.2),
    Note(38, 100, 5 * beat_time, 0.2),
    Note(38, 100, 7 * beat_time, 0.2),
]
for note in snare_notes:
    drum_instr.notes.append(note)

hihat_notes = [
    Note(42, 100, 0, 0.15),
    Note(42, 100, beat_time, 0.15),
    Note(42, 100, 2 * beat_time, 0.15),
    Note(42, 100, 3 * beat_time, 0.15),
    Note(42, 100, 4 * beat_time, 0.15),
    Note(42, 100, 5 * beat_time, 0.15),
    Note(42, 100, 6 * beat_time, 0.15),
    Note(42, 100, 7 * beat_time, 0.15),
]
for note in hihat_notes:
    drum_instr.notes.append(note)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    Note(62, 100, 0, 0.5),  # F#4
    Note(65, 100, 0.75, 0.25),  # A4
    Note(62, 100, 2 * beat_time, 0.5),  # F#4
    Note(65, 100, 2.75, 0.25),  # A4
    Note(67, 100, 4 * beat_time, 0.5),  # Bb4
    Note(65, 100, 4.75, 0.25),  # A4
    Note(62, 100, 5.5, 0.5),  # F#4
    Note(67, 100, 6.3, 0.2),  # Bb4
]
for note in sax_notes:
    sax_instr.notes.append(note)

# Write the MIDI file
pm.write("jazz_intro.mid")
