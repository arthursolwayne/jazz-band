
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
bass = Instrument(program=Program.FROM_PROGRAM, program=33)  # Electric Bass
sax = Instrument(program=Program.TENOR_SAX)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(sax)

# Define timing
BPM = 160
notes_per_beat = 4  # 4/4 time
beat = pretty_midi.time_to_tick(60.0 / BPM, pm.resolution)
bar = beat * 4

# Drums: Kick on 1 & 3, snare on 2 & 4, hihat on all eighths
drum_notes = {
    # Kick on 1 & 3
    0: Note(36, 100, 0, beat),
    beat * 2: Note(36, 100, 0, beat),
    # Snare on 2 & 4
    beat: Note(38, 100, 0, beat),
    beat * 3: Note(38, 100, 0, beat),
    # Hi-hat on all eighths
    0: Note(42, 80, 0, beat / 2),
    beat / 2: Note(42, 80, 0, beat / 2),
    beat: Note(42, 80, 0, beat / 2),
    beat * 3 / 2: Note(42, 80, 0, beat / 2),
    beat * 2: Note(42, 80, 0, beat / 2),
    beat * 5 / 2: Note(42, 80, 0, beat / 2),
    beat * 3: Note(42, 80, 0, beat / 2),
    beat * 7 / 2: Note(42, 80, 0, beat / 2)
}

for time, note in drum_notes.items():
    drums.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 & 4
# Bar 1: No piano
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bbm7 (Bb, Db, F, Ab)
# Bar 4: Ebm7 (Eb, Gb, Bb, Db)
piano_notes = []
bar_start = beat * 1  # bar 2
notes = [65, 69, 72, 67]  # Fm7: F, Ab, C, Eb
for i, note in enumerate(notes):
    piano_notes.append(Note(note, 90, bar_start + beat * 0.25 * i, beat * 0.25))
bar_start = beat * 2  # bar 3
notes = [71, 74, 65, 69]  # Bbm7: Bb, Db, F, Ab
for i, note in enumerate(notes):
    piano_notes.append(Note(note, 90, bar_start + beat * 0.25 * i, beat * 0.25))
bar_start = beat * 3  # bar 4
notes = [67, 70, 71, 74]  # Ebm7: Eb, Gb, Bb, Db
for i, note in enumerate(notes):
    piano_notes.append(Note(note, 90, bar_start + beat * 0.25 * i, beat * 0.25))

for note in piano_notes:
    piano.notes.append(note)

# Bass (Marcus): Walking line with chromatic approach
# Start on F (bar 1, beat 1)
bass_notes = []

# Bar 1 (build tension)
bass_notes.append(Note(65, 70, 0, beat))  # F
bass_notes.append(Note(64, 70, beat, beat / 2))  # Fb (chromatic)
bass_notes.append(Note(65, 70, beat / 2, beat / 2))  # F

# Bar 2 (walking line)
bass_notes.append(Note(72, 70, beat, beat))  # C
bass_notes.append(Note(71, 70, beat * 2, beat))  # Bb
bass_notes.append(Note(72, 70, beat * 3, beat))  # C
bass_notes.append(Note(69, 70, beat * 4, beat))  # Ab

# Bar 3
bass_notes.append(Note(67, 70, beat * 4, beat))  # Eb
bass_notes.append(Note(68, 70, beat * 5, beat))  # F
bass_notes.append(Note(70, 70, beat * 6, beat))  # Gb
bass_notes.append(Note(69, 70, beat * 7, beat))  # Ab

# Bar 4
bass_notes.append(Note(65, 70, beat * 8, beat))  # F
bass_notes.append(Note(64, 70, beat * 9, beat))  # Fb
bass_notes.append(Note(65, 70, beat * 10, beat))  # F
bass_notes.append(Note(64, 70, beat * 11, beat))  # Fb

for note in bass_notes:
    bass.notes.append(note)

# Sax (You): Short motif, space, question
# F (65), Ab (69), C (72), with a rest
sax_notes = [
    Note(65, 100, 0, beat),  # F
    Note(69, 100, beat, beat),  # Ab
    Note(72, 100, beat * 2, beat),  # C
    Note(69, 100, beat * 3, beat),  # Ab
    Note(65, 100, beat * 4, beat),  # F
    Note(65, 100, beat * 5, beat),  # F (sustained)
    Note(69, 100, beat * 6, beat),  # Ab
    Note(72, 100, beat * 7, beat)   # C
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro_Fm.mid')
