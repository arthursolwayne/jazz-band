
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D Major
# Program changes: Use appropriate instruments
# Drums (Percussive)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_inst = Instrument(program=drum_program, is_drum=True)
midi.instruments.append(drum_inst)

# Bass (Acoustic Bass)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_inst = Instrument(program=bass_program)
midi.instruments.append(bass_inst)

# Piano (Electric Piano)
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
piano_inst = Instrument(program=piano_program)
midi.instruments.append(piano_inst)

# Tenor Sax (Alto Sax for simplicity)
sax_program = pretty_midi.instrument_name_to_program('Alto Saxophone')
sax_inst = Instrument(program=sax_program)
midi.instruments.append(sax_inst)

# Set up the tempo (160 BPM)
midi.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Timing constants
BPM = 160
BEAT = 60 / BPM  # in seconds
BAR = 4 * BEAT  # 4 beats per bar
BAR_DURATION = 1.5  # 6 seconds for 4 bars
TIME_INCREMENT = BEAT / 4  # 16th note duration

# Bar 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time: 0s to 1.5s (bar duration)
for bar in range(1):
    time = bar * BAR_DURATION
    # Kick on beat 1 and 3
    kick_1 = Note(26, 0.2, time + 0)
    kick_3 = Note(26, 0.2, time + 2 * BEAT)
    # Snare on beat 2 and 4
    snare_2 = Note(38, 0.2, time + 1 * BEAT)
    snare_4 = Note(38, 0.2, time + 3 * BEAT)
    # Hi-hats on every 8th
    for i in range(8):
        hihat = Note(42, 0.05, time + i * TIME_INCREMENT)
        drum_inst.notes.append(hihat)
    drum_inst.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bar 2: All instruments in
# Bar starts at 1.5s
time = 1.5

# Bass line (Marcus): Walking line, chromatic approaches, no repeating notes
# D Dorian: D, E, F#, G, A, B, C
bass_notes = [
    Note(62, 0.5, time + 0),       # D
    Note(63, 0.5, time + BEAT),    # E
    Note(61, 0.5, time + 2 * BEAT), # F#
    Note(64, 0.5, time + 3 * BEAT), # G
    Note(67, 0.5, time + 4 * BEAT), # A
    Note(69, 0.5, time + 5 * BEAT), # B
    Note(67, 0.5, time + 6 * BEAT), # A
    Note(65, 0.5, time + 7 * BEAT), # Bb (chromatic approach)
]
bass_inst.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# D7 chord: D, F#, A, C
# Chord voicings on beats 2 and 4 only
piano_notes = [
    # Beat 2: D7
    Note(62, 0.5, time + 1 * BEAT), # D
    Note(66, 0.5, time + 1 * BEAT), # F#
    Note(67, 0.5, time + 1 * BEAT), # A
    Note(65, 0.5, time + 1 * BEAT), # C
    # Beat 4: D7 (with altered extension)
    Note(69, 0.5, time + 3 * BEAT), # B (altered)
    Note(64, 0.5, time + 3 * BEAT), # G (root)
    Note(66, 0.5, time + 3 * BEAT), # F#
    Note(67, 0.5, time + 3 * BEAT), # A
]
piano_inst.notes.extend(piano_notes)

# Tenor Sax (Dante): Melody, one short motif, leave it hanging
# Dorian mode: D, E, F#, G, A, B, C
# Motif: D - E - F# (half note on D, eighth on E, eighth on F#) on beat 1
# Then rest for the rest of the bar — create anticipation

sax_notes = [
    Note(62, 1.0, time + 0),  # D (half note)
    Note(63, 0.5, time + 1 * TIME_INCREMENT),  # E (eighth note)
    Note(65, 0.5, time + 2 * TIME_INCREMENT),  # F# (eighth note)
]
sax_inst.notes.extend(sax_notes)

# Write the MIDI file
midi.write("dante_intro.mid")
print("Generated MIDI file: 'dante_intro.mid'")
