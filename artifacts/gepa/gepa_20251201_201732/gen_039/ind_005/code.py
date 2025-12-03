
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 60 / 160 * 4  # 6 seconds per 4 bars
beat_length = bar_length / 4  # 1.5 seconds per beat

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36]  # MIDI note for kick drum
snare_notes = [38]  # MIDI note for snare
hihat_notes = [42]  # MIDI note for hihat

# Create kick on beats 1 and 3 of each bar
for bar in range(4):
    kick_time = bar * bar_length + beat_length * (1 - 1)
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=kick_time, end=kick_time + 0.1)
    bass.notes.append(kick)

    kick_time = bar * bar_length + beat_length * (3 - 1)
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=kick_time, end=kick_time + 0.1)
    bass.notes.append(kick)

# Create snare on beats 2 and 4 of each bar
for bar in range(4):
    snare_time = bar * bar_length + beat_length * (2 - 1)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[0], start=snare_time, end=snare_time + 0.1)
    bass.notes.append(snare)

    snare_time = bar * bar_length + beat_length * (4 - 1)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[0], start=snare_time, end=snare_time + 0.1)
    bass.notes.append(snare)

# Hihat on every eighth note
for bar in range(4):
    for beat in range(4):
        for eighth in range(2):
            hihat_time = bar * bar_length + beat * beat_length + eighth * beat_length / 2
            hihat = pretty_midi.Note(velocity=100, pitch=hihat_notes[0], start=hihat_time, end=hihat_time + 0.05)
            bass.notes.append(hihat)

pm.instruments.append(bass)

# --- BASS: Marcus ---
# Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Chord progression for Dm: Dm - Gm7 - Cm7 - F7
# Root movement: D -> G -> C -> F

# Bar 1: Dm -> Gm7
# Bar 2: Cm7
# Bar 3: F7
# Bar 4: Dm

# Bar 1 (Dm)
root = 38  # D2
fifth = 43  # A2
root_time = 0
note = pretty_midi.Note(velocity=90, pitch=root, start=root_time, end=root_time + 0.25)
bass.notes.append(note)

# Chromatic approach to fifth
approach = 42  # G#2
approach_time = root_time + 0.1
note = pretty_midi.Note(velocity=85, pitch=approach, start=approach_time, end=approach_time + 0.1)
bass.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=fifth, start=approach_time + 0.1, end=approach_time + 0.2)
bass.notes.append(note)

# Bar 2 (Gm7)
root = 43  # G2
fifth = 48  # D3
root_time = beat_length * 1
note = pretty_midi.Note(velocity=90, pitch=root, start=root_time, end=root_time + 0.25)
bass.notes.append(note)

approach = 44  # A2
approach_time = root_time + 0.1
note = pretty_midi.Note(velocity=85, pitch=approach, start=approach_time, end=approach_time + 0.1)
bass.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=fifth, start=approach_time + 0.1, end=approach_time + 0.2)
bass.notes.append(note)

# Bar 3 (Cm7)
root = 40  # C2
fifth = 45  # G2
root_time = beat_length * 2
note = pretty_midi.Note(velocity=90, pitch=root, start=root_time, end=root_time + 0.25)
bass.notes.append(note)

approach = 39  # Bb2
approach_time = root_time + 0.1
note = pretty_midi.Note(velocity=85, pitch=approach, start=approach_time, end=approach_time + 0.1)
bass.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=fifth, start=approach_time + 0.1, end=approach_time + 0.2)
bass.notes.append(note)

# Bar 4 (F7)
root = 46  # F2
fifth = 51  # C3
root_time = beat_length * 3
note = pretty_midi.Note(velocity=90, pitch=root, start=root_time, end=root_time + 0.25)
bass.notes.append(note)

approach = 45  # E2
approach_time = root_time + 0.1
note = pretty_midi.Note(velocity=85, pitch=approach, start=approach_time, end=approach_time + 0.1)
bass.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=fifth, start=approach_time + 0.1, end=approach_time + 0.2)
bass.notes.append(note)

pm.instruments.append(bass)

# --- PIANO: Diane ---
# Open voicings, different chord each bar, resolve on the last

# Bar 1: Dm (Dm7)
# Dm7: D F A C
chord_notes = [50, 53, 57, 60]
time = 0
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(piano_note)

# Bar 2: Gm7 (G Bb D F)
chord_notes = [55, 57, 62, 65]
time = beat_length * 1
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(piano_note)

# Bar 3: Cm7 (C Eb G Bb)
chord_notes = [52, 55, 60, 63]
time = beat_length * 2
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(piano_note)

# Bar 4: F7 (F A C E)
chord_notes = [54, 57, 60, 64]
time = beat_length * 3
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(piano_note)

pm.instruments.append(piano)

# --- SAX: You ---
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 1: Start the motif
note1 = pretty_midi.Note(velocity=110, pitch=62, start=0, end=0.3)
sax.notes.append(note1)

# Bar 2: Leave it hanging
# No notes in bar 2

# Bar 3: Come back and finish it
note1 = pretty_midi.Note(velocity=110, pitch=62, start=beat_length * 2, end=beat_length * 2 + 0.3)
sax.notes.append(note1)

# Bar 4: Continue the motif with a resolution
note2 = pretty_midi.Note(velocity=110, pitch=60, start=beat_length * 3, end=beat_length * 3 + 0.3)
sax.notes.append(note2)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
