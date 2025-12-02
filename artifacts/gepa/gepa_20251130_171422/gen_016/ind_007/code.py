
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time per beat and bar
BPM = 160
BEATS_PER_BAR = 4
SECONDS_PER_BEAT = 60.0 / BPM
SECONDS_PER_BAR = BEATS_PER_BAR * SECONDS_PER_BEAT

# Create instruments
drums = Instrument(program=Program.DRUM_SET, is_drum=True)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.ACOUSTIC_PIANO)
sax = Instrument(program=Program.TENOR_SAXOPHONE)

pm.instruments = [drums, bass, piano, sax]

# Helper function to add a note to an instrument
def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# Bar 1: Drums only (4/4 time, kick on 1 and 3, snare on 2 and 4, hihat every 8th)
bar_1_start = 0
bar_1_end = SECONDS_PER_BAR

# Kick on 1 and 3 (beat 0 and 2)
add_note(drums, 36, bar_1_start, bar_1_start + SECONDS_PER_BEAT, 100)
add_note(drums, 36, bar_1_start + 2 * SECONDS_PER_BEAT, bar_1_start + 3 * SECONDS_PER_BEAT, 100)

# Snare on 2 and 4 (beat 1 and 3)
add_note(drums, 38, bar_1_start + SECONDS_PER_BEAT, bar_1_start + SECONDS_PER_BEAT + 0.1, 100)
add_note(drums, 38, bar_1_start + 3 * SECONDS_PER_BEAT, bar_1_start + 3 * SECONDS_PER_BEAT + 0.1, 100)

# Hihat on every eighth note
for i in range(0, 8):
    add_note(drums, 42, bar_1_start + i * SECONDS_PER_BEAT / 2, bar_1_start + i * SECONDS_PER_BEAT / 2 + 0.05, 80)

# Bar 2: Everyone in, sax starts the motif
bar_2_start = bar_1_end

# Sax melody (D major, short motif)
# D - F# - G - A - D (Dorian mode-like, a little dark)
# Time: 1-2-3-4-1 (over 4 beats)
add_note(sax, 62, bar_2_start, bar_2_start + SECONDS_PER_BEAT, 100)
add_note(sax, 67, bar_2_start + SECONDS_PER_BEAT, bar_2_start + 2 * SECONDS_PER_BEAT, 100)
add_note(sax, 69, bar_2_start + 2 * SECONDS_PER_BEAT, bar_2_start + 3 * SECONDS_PER_BEAT, 100)
add_note(sax, 71, bar_2_start + 3 * SECONDS_PER_BEAT, bar_2_start + 4 * SECONDS_PER_BEAT, 100)
add_note(sax, 62, bar_2_start + 4 * SECONDS_PER_BEAT, bar_2_start + 4.5 * SECONDS_PER_BEAT, 100)

# Bass walking line (chromatic from D to G)
# D - Eb - E - F - G (chromatic approach to G, resolves to F#)
notes = [62, 63, 64, 65, 67]
for i, pitch in enumerate(notes):
    start = bar_2_start + i * SECONDS_PER_BEAT
    end = start + SECONDS_PER_BEAT
    add_note(bass, pitch, start, end, 80)

# Piano: 7th chords on beats 2 and 4
# Bar 2: D7 on beat 2
# Bar 3: G7 on beat 4
# Bar 4: C7 on beat 2

# Bar 2: D7 (D - F# - A - C)
add_note(piano, 62, bar_2_start + SECONDS_PER_BEAT, bar_2_start + 1.1, 100)
add_note(piano, 67, bar_2_start + SECONDS_PER_BEAT, bar_2_start + 1.1, 100)
add_note(piano, 69, bar_2_start + SECONDS_PER_BEAT, bar_2_start + 1.1, 100)
add_note(piano, 64, bar_2_start + SECONDS_PER_BEAT, bar_2_start + 1.1, 100)

# Bar 3: G7 (G - B - D - F)
add_note(piano, 67, bar_2_start + 2 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 2 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 71, bar_2_start + 2 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 2 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 69, bar_2_start + 2 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 2 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 65, bar_2_start + 2 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 2 * SECONDS_PER_BEAT + 1.1, 100)

# Bar 4: C7 (C - E - G - B)
add_note(piano, 60, bar_2_start + 3 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 3 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 64, bar_2_start + 3 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 3 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 67, bar_2_start + 3 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 3 * SECONDS_PER_BEAT + 1.1, 100)
add_note(piano, 71, bar_2_start + 3 * SECONDS_PER_BEAT + SECONDS_PER_BEAT, bar_2_start + 3 * SECONDS_PER_BEAT + 1.1, 100)

# Bar 4: Drums still going, drum pattern repeated
bar_4_start = bar_2_start + 2 * SECONDS_PER_BAR
bar_4_end = bar_4_start + SECONDS_PER_BAR

# Kick on 1 and 3 (beat 0 and 2)
add_note(drums, 36, bar_4_start, bar_4_start + SECONDS_PER_BEAT, 100)
add_note(drums, 36, bar_4_start + 2 * SECONDS_PER_BEAT, bar_4_start + 3 * SECONDS_PER_BEAT, 100)

# Snare on 2 and 4 (beat 1 and 3)
add_note(drums, 38, bar_4_start + SECONDS_PER_BEAT, bar_4_start + SECONDS_PER_BEAT + 0.1, 100)
add_note(drums, 38, bar_4_start + 3 * SECONDS_PER_BEAT, bar_4_start + 3 * SECONDS_PER_BEAT + 0.1, 100)

# Hihat on every eighth note
for i in range(0, 8):
    add_note(drums, 42, bar_4_start + i * SECONDS_PER_BEAT / 2, bar_4_start + i * SECONDS_PER_BEAT / 2 + 0.05, 80)

# Save the MIDI
pm.write('dante_intro.mid')
