
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D minor (key number 19 in MIDI)
pm.key_signature_changes = [pretty_midi.KeySignature(19, 0)]

# Set the time resolution to 1/4 note (since 160 BPM = 60/160 = 0.375s per beat)
pm.resolution = 480  # standard MIDI resolution

### 🥁 DRUMS (Little Ray)
drum_program = Program(0, 0)  # Program 0 = Acoustic Grand Piano, but we'll use instrument change for drums
drum_inst = Instrument(program=Program(128, 0), is_drum=True)
pm.instruments.append(drum_inst)

# Define the drum notes for 4 bars (160 BPM, 4/4 time, 6 seconds)
# Each bar = 4 beats = 4 * 480 / 160 = 12 notes per beat * 4 = 48 notes per bar

# Kick on 1 and 3 of each bar
kick_notes = [Note(36, 100, 0, 0.375),  # Bar 1, beat 1
              Note(36, 100, 1.5, 0.375), # Bar 1, beat 3
              Note(36, 100, 3.0, 0.375), # Bar 2, beat 1
              Note(36, 100, 4.5, 0.375), # Bar 2, beat 3
              Note(36, 100, 6.0, 0.375), # Bar 3, beat 1
              Note(36, 100, 7.5, 0.375), # Bar 3, beat 3
              Note(36, 100, 9.0, 0.375), # Bar 4, beat 1
              Note(36, 100, 10.5, 0.375)] # Bar 4, beat 3

# Snare on 2 and 4 of each bar
snare_notes = [Note(38, 100, 0.75, 0.375), # Bar 1, beat 2
               Note(38, 100, 2.25, 0.375), # Bar 1, beat 4
               Note(38, 100, 3.75, 0.375), # Bar 2, beat 2
               Note(38, 100, 5.25, 0.375), # Bar 2, beat 4
               Note(38, 100, 6.75, 0.375), # Bar 3, beat 2
               Note(38, 100, 8.25, 0.375), # Bar 3, beat 4
               Note(38, 100, 10.5, 0.375), # Bar 4, beat 4
               Note(38, 100, 12.0, 0.375)] # Bar 4, beat 4 (optional for punch)

# Hihat on every 8th note
hihat_notes = [Note(42, 80, 0, 0.1875),    # Beat 1/8
               Note(42, 80, 0.375, 0.1875), # Beat 2/8
               Note(42, 80, 0.75, 0.1875),  # Beat 3/8
               Note(42, 80, 1.125, 0.1875), # Beat 4/8
               Note(42, 80, 1.5, 0.1875),   # Beat 5/8
               Note(42, 80, 1.875, 0.1875), # Beat 6/8
               Note(42, 80, 2.25, 0.1875),  # Beat 7/8
               Note(42, 80, 2.625, 0.1875), # Beat 8/8

               Note(42, 80, 3.0, 0.1875),
               Note(42, 80, 3.375, 0.1875),
               Note(42, 80, 3.75, 0.1875),
               Note(42, 80, 4.125, 0.1875),
               Note(42, 80, 4.5, 0.1875),
               Note(42, 80, 4.875, 0.1875),
               Note(42, 80, 5.25, 0.1875),
               Note(42, 80, 5.625, 0.1875),

               Note(42, 80, 6.0, 0.1875),
               Note(42, 80, 6.375, 0.1875),
               Note(42, 80, 6.75, 0.1875),
               Note(42, 80, 7.125, 0.1875),
               Note(42, 80, 7.5, 0.1875),
               Note(42, 80, 7.875, 0.1875),
               Note(42, 80, 8.25, 0.1875),
               Note(42, 80, 8.625, 0.1875),

               Note(42, 80, 9.0, 0.1875),
               Note(42, 80, 9.375, 0.1875),
               Note(42, 80, 9.75, 0.1875),
               Note(42, 80, 10.125, 0.1875),
               Note(42, 80, 10.5, 0.1875),
               Note(42, 80, 10.875, 0.1875),
               Note(42, 80, 11.25, 0.1875),
               Note(42, 80, 11.625, 0.1875)]

# Add the notes to the drum instrument
for note in kick_notes:
    drum_inst.notes.append(note)
for note in snare_notes:
    drum_inst.notes.append(note)
for note in hihat_notes:
    drum_inst.notes.append(note)

### 🎸 BASS (Marcus)
bass_program = Program(33, 0)  # Electric Bass
bass_inst = Instrument(program=bass_program)
pm.instruments.append(bass_inst)

# D minor bass line: D, Eb, F, G, A, Bb, C, D
# Walking bass line with chromatic approaches
bass_notes = [
    # Bar 1:
    Note(62, 80, 0, 0.375),  # D (2nd beat)
    Note(60, 80, 0.75, 0.375), # Eb
    Note(61, 80, 1.125, 0.375), # F
    Note(62, 80, 1.5, 0.75),   # G (rest on 1.5, then G on 2.25)

    # Bar 2:
    Note(64, 80, 2.25, 0.375),  # A
    Note(62, 80, 2.625, 0.375), # Bb (chromatic)
    Note(60, 80, 3.0, 0.375),   # D
    Note(62, 80, 3.375, 0.375), # Eb

    # Bar 3:
    Note(61, 80, 3.75, 0.375),  # F
    Note(62, 80, 4.125, 0.375), # G
    Note(64, 80, 4.5, 0.375),   # A
    Note(63, 80, 4.875, 0.375), # Bb (chromatic)

    # Bar 4:
    Note(62, 80, 5.25, 0.375),  # D
    Note(60, 80, 5.625, 0.375), # Eb
    Note(61, 80, 6.0, 0.375),   # F
    Note(62, 80, 6.375, 0.375), # G
]

for note in bass_notes:
    bass_inst.notes.append(note)

### 🎹 PIANO (Diane)
piano_program = Program(0, 0)  # Acoustic Grand Piano
piano_inst = Instrument(program=piano_program)
pm.instruments.append(piano_inst)

# Diane's comping: 7th chords on 2 and 4, with some dissonance
# Dm7 = D, F, A, C
# Gm7 = G, Bb, D, F
# Am7 = A, C, E, G
# Cm7 = C, Eb, G, Bb

# Bar 1:
# Comp on beat 2 (Dm7) and beat 4 (Gm7)
piano_notes = [
    Note(62, 100, 0.75, 0.375), # D
    Note(65, 100, 0.75, 0.375), # F
    Note(67, 100, 0.75, 0.375), # A
    Note(60, 100, 0.75, 0.375), # C

    Note(67, 100, 2.25, 0.375), # G
    Note(65, 100, 2.25, 0.375), # Bb
    Note(62, 100, 2.25, 0.375), # D
    Note(65, 100, 2.25, 0.375), # F
]

# Bar 2:
# Comp on beat 2 (Am7) and beat 4 (Cm7)
piano_notes.extend([
    Note(69, 100, 3.75, 0.375), # A
    Note(60, 100, 3.75, 0.375), # C
    Note(64, 100, 3.75, 0.375), # E
    Note(67, 100, 3.75, 0.375), # G

    Note(60, 100, 5.25, 0.375), # C
    Note(62, 100, 5.25, 0.375), # Eb
    Note(67, 100, 5.25, 0.375), # G
    Note(65, 100, 5.25, 0.375), # Bb
])

# Bar 3:
# Comp on beat 2 (Dm7) and beat 4 (Gm7)
piano_notes.extend([
    Note(62, 100, 6.75, 0.375), # D
    Note(65, 100, 6.75, 0.375), # F
    Note(67, 100, 6.75, 0.375), # A
    Note(60, 100, 6.75, 0.375), # C

    Note(67, 100, 8.25, 0.375), # G
    Note(65, 100, 8.25, 0.375), # Bb
    Note(62, 100, 8.25, 0.375), # D
    Note(65, 100, 8.25, 0.375), # F
])

# Bar 4:
# Comp on beat 2 (Am7) and beat 4 (Cm7)
piano_notes.extend([
    Note(69, 100, 9.75, 0.375), # A
    Note(60, 100, 9.75, 0.375), # C
    Note(64, 100, 9.75, 0.375), # E
    Note(67, 100, 9.75, 0.375), # G

    Note(60, 100, 11.25, 0.375), # C
    Note(62, 100, 11.25, 0.375), # Eb
    Note(67, 100, 11.25, 0.375), # G
    Note(65, 100, 11.25, 0.375), # Bb
])

for note in piano_notes:
    piano_inst.notes.append(note)

### 🎶 SAX (You)
sax_program = Program(64, 0)  # Tenor Saxophone
sax_inst = Instrument(program=sax_program)
pm.instruments.append(sax_inst)

# Your motif — simple, sparse, with silence
# Bar 1: Play a short phrase — D, Eb, F, G
# Bar 2: Rest
# Bar 3: Repeat — D, Eb, F, G (with a slight delay)
# Bar 4: End with a held note (A) — lingering

sax_notes = [
    Note(62, 110, 0, 0.375),  # D
    Note(60, 110, 0.75, 0.375), # Eb
    Note(61, 110, 1.125, 0.375), # F
    Note(62, 110, 1.5, 0.375),  # G

    # Bar 3:
    Note(62, 110, 6.0, 0.375),  # D
    Note(60, 110, 6.75, 0.375), # Eb
    Note(61, 110, 7.125, 0.375), # F
    Note(62, 110, 7.5, 0.375),  # G

    # Bar 4:
    Note(64, 110, 9.0, 1.5),  # A — held for the final 1.5 seconds
]

for note in sax_notes:
    sax_inst.notes.append(note)

# Save the MIDI file
pm.write("4_bar_intro_d_minor.mid")

print("MIDI file generated: '4_bar_intro_d_minor.mid'")
