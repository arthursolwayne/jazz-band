
import mido
from mido import Message, MidiFile, MidiTrack
import time

# Create a MIDI file
mid = MidiFile()
track = MidiTrack()
mid.add_track(track)

# Set tempo (160 BPM)
# MIDI tempo is in microseconds per beat
tempo = mido.bpm2tempo(160)
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Time signatures
track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notations=0))

# Key signature - D minor (1 flat)
track.append(mido.MetaMessage('key_signature', key='D', scale='minor', mode='minor', fifths=-1))

# Define the time per beat (in ticks)
# Using standard MIDI ticks per beat (480)
ticks_per_beat = 480
bar_length = ticks_per_beat * 4  # 4 bars = 16 beats = 6.0 seconds at 160 BPM
tick_per_beat = ticks_per_beat / 160 * 60  # ticks per second (approximate, for timing)

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_program = 0
drum_track = MidiTrack()
mid.add_track(drum_track)
drum_track.append(mido.Message('program_change', program=drum_program, channel=9))

def kick(beat):
    drum_track.append(Message('note_on', note=36, velocity=100, time=beat, channel=9))
    drum_track.append(Message('note_off', note=36, velocity=100, time=1, channel=9))

def snare(beat):
    drum_track.append(Message('note_on', note=38, velocity=100, time=beat, channel=9))
    drum_track.append(Message('note_off', note=38, velocity=100, time=1, channel=9))

def hihat(beat):
    drum_track.append(Message('note_on', note=42, velocity=90, time=beat, channel=9))
    drum_track.append(Message('note_off', note=42, velocity=90, time=1, channel=9))

# Bar 1: Just hihat on every eighth
for i in range(0, bar_length, ticks_per_beat // 8):
    hihat(i)

# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_start = bar_length
for i in range(0, bar_length, ticks_per_beat // 8):
    if i % ticks_per_beat == 0:  # beat 1
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2:  # beat 2
        snare(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 4 * 3:  # beat 3
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2 * 3:  # beat 4
        snare(i)
        hihat(i)

# Bar 3: Same as bar 2
bar3_start = bar2_start + bar_length
for i in range(0, bar_length, ticks_per_beat // 8):
    if i % ticks_per_beat == 0:  # beat 1
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2:  # beat 2
        snare(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 4 * 3:  # beat 3
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2 * 3:  # beat 4
        snare(i)
        hihat(i)

# Bar 4: Same as bar 2
bar4_start = bar3_start + bar_length
for i in range(0, bar_length, ticks_per_beat // 8):
    if i % ticks_per_beat == 0:  # beat 1
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2:  # beat 2
        snare(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 4 * 3:  # beat 3
        kick(i)
        hihat(i)
    elif i % ticks_per_beat == ticks_per_beat // 2 * 3:  # beat 4
        snare(i)
        hihat(i)

# --- BASS: Marcus ---
# Walking line, roots and fifths with chromatic approaches
bass_program = 33
bass_track = MidiTrack()
mid.add_track(bass_track)
bass_track.append(mido.Message('program_change', program=bass_program, channel=0))

# Bar 1: Dm7 - D, A (Fifth), C (chromatic approach), D, A
notes = [62, 67, 61, 62, 67]  # D, A, C, D, A
for note in notes:
    bass_track.append(Message('note_on', note=note, velocity=80, time=0, channel=0))
    bass_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat // 4, channel=0))

# Bar 2: Gm7 - G, D, F, G, D
notes = [67, 72, 66, 67, 72]
for note in notes:
    bass_track.append(Message('note_on', note=note, velocity=80, time=0, channel=0))
    bass_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat // 4, channel=0))

# Bar 3: Cm7 - C, G, Bb, C, G
notes = [60, 67, 62, 60, 67]
for note in notes:
    bass_track.append(Message('note_on', note=note, velocity=80, time=0, channel=0))
    bass_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat // 4, channel=0))

# Bar 4: F7 - F, C, Eb, F, C
notes = [65, 72, 67, 65, 72]
for note in notes:
    bass_track.append(Message('note_on', note=note, velocity=80, time=0, channel=0))
    bass_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat // 4, channel=0))

# --- PIANO: Diane ---
# Open voicings, one chord per bar, resolve on the last
piano_program = 0
piano_track = MidiTrack()
mid.add_track(piano_track)
piano_track.append(mido.Message('program_change', program=piano_program, channel=1))

# Bar 1: Dm7 (D, F, A, C)
notes = [62, 66, 67, 60]
for note in notes:
    piano_track.append(Message('note_on', note=note, velocity=80, time=0, channel=1))
for note in notes:
    piano_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat, channel=1))

# Bar 2: Gm7 (G, Bb, D, F)
notes = [67, 62, 72, 66]
for note in notes:
    piano_track.append(Message('note_on', note=note, velocity=80, time=0, channel=1))
for note in notes:
    piano_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat, channel=1))

# Bar 3: Cm7 (C, Eb, G, Bb)
notes = [60, 64, 67, 62]
for note in notes:
    piano_track.append(Message('note_on', note=note, velocity=80, time=0, channel=1))
for note in notes:
    piano_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat, channel=1))

# Bar 4: F7 (F, A, C, Eb)
notes = [65, 67, 72, 64]
for note in notes:
    piano_track.append(Message('note_on', note=note, velocity=80, time=0, channel=1))
for note in notes:
    piano_track.append(Message('note_off', note=note, velocity=80, time=ticks_per_beat, channel=1))

# --- SAX: You ---
# Tenor sax - D minor, 4 bars, one short motif with space
sax_program = 64
sax_track = MidiTrack()
mid.add_track(sax_track)
sax_track.append(mido.Message('program_change', program=sax_program, channel=2))

# Bar 1: Rest (no notes)
sax_track.append(Message('note_on', note=60, velocity=0, time=0, channel=2))
sax_track.append(Message('note_off', note=60, velocity=0, time=ticks_per_beat, channel=2))

# Bar 2: First motif - D, F, A (Dm7), rest on beat 4
notes = [62, 66, 67]
for note in notes:
    sax_track.append(Message('note_on', note=note, velocity=100, time=0, channel=2))
    sax_track.append(Message('note_off', note=note, velocity=100, time=ticks_per_beat // 4, channel=2))
sax_track.append(Message('note_on', note=60, velocity=0, time=0, channel=2))
sax_track.append(Message('note_off', note=60, velocity=0, time=ticks_per_beat // 4 * 3, channel=2))

# Bar 3: Rest
sax_track.append(Message('note_on', note=60, velocity=0, time=0, channel=2))
sax_track.append(Message('note_off', note=60, velocity=0, time=ticks_per_beat, channel=2))

# Bar 4: Second motif - D, F, A, C (Dm7), resolve on C
notes = [62, 66, 67, 60]
for note in notes:
    sax_track.append(Message('note_on', note=note, velocity=100, time=0, channel=2))
    sax_track.append(Message('note_off', note=note, velocity=100, time=ticks_per_beat // 4, channel=2))

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file 'dante_intro.mid' created.")
