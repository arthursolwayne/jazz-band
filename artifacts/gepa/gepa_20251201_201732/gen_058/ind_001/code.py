
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define the time per bar (1.5 seconds at 160 BPM)
bar_length = 1.5

# Define the key: F minor (but we'll use F major with a twist of minor feel)
# F major scale: F, G, A, Bb, B, C, D
# But we'll play with tension and unresolved chords

# Duration in seconds
note_duration = 0.375  # 1/8 note at 160 BPM

# --- DRUMS: Little Ray
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same pattern, but with a fill on beat 3 of bar 2

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_duration))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=note_duration, end=note_duration*2))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0, end=note_duration*4))  # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=note_duration*2, end=note_duration*3))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=note_duration*3, end=note_duration*4))  # Snare on 4

# Bar 2: with a fill on beat 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length, end=bar_length + note_duration))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length + note_duration, end=bar_length + note_duration*2))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_length, end=bar_length + note_duration*4))  # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length + note_duration*2, end=bar_length + note_duration*3))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length + note_duration*3, end=bar_length + note_duration*4))  # Snare on 4
# Fill on beat 3 of bar 2
drums.notes.append(pretty_midi.Note(velocity=110, pitch=46, start=bar_length + note_duration*2, end=bar_length + note_duration*2 + 0.2))  # cymbal fill
drums.notes.append(pretty_midi.Note(velocity=110, pitch=48, start=bar_length + note_duration*2 + 0.2, end=bar_length + note_duration*2 + 0.4))  # cymbal fill

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length*2, end=bar_length*2 + note_duration))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_length*2, end=bar_length*2 + note_duration*4))  # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length*2 + note_duration*2, end=bar_length*2 + note_duration*3))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length*2 + note_duration*3, end=bar_length*2 + note_duration*4))  # Snare on 4

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length*3, end=bar_length*3 + note_duration))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_length*3, end=bar_length*3 + note_duration*4))  # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_length*3 + note_duration*2, end=bar_length*3 + note_duration*3))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_length*3 + note_duration*3, end=bar_length*3 + note_duration*4))  # Snare on 4

# --- BASS: Marcus
# Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Bar 1: F - G - C - G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0, end=note_duration))  # F (root)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=note_duration, end=note_duration*2))  # G (fifth)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=note_duration*2, end=note_duration*3))  # C (octave)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=note_duration*3, end=note_duration*4))  # G (fifth)

# Bar 2: C - Bb - C - Ab
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar_length, end=bar_length + note_duration))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=bar_length + note_duration, end=bar_length + note_duration*2))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar_length + note_duration*2, end=bar_length + note_duration*3))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=bar_length + note_duration*3, end=bar_length + note_duration*4))  # Ab

# Bar 3: F - G - C - G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_length*2, end=bar_length*2 + note_duration))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar_length*2 + note_duration*2, end=bar_length*2 + note_duration*3))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=bar_length*2 + note_duration*3, end=bar_length*2 + note_duration*4))  # G

# Bar 4: C - Bb - C - Ab
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar_length*3, end=bar_length*3 + note_duration))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar_length*3 + note_duration*2, end=bar_length*3 + note_duration*3))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=bar_length*3 + note_duration*3, end=bar_length*3 + note_duration*4))  # Ab

# --- PIANO: Diane
# Open voicings, different chord each bar, resolve on the last
# Comp on 2 and 4

# Bar 1: F7 (F-A-C-Eb)
# Open voicing: F, A, Eb, C
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=note_duration, end=note_duration*2))  # A
piano.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=note_duration, end=note_duration*2))  # F
piano.notes.append(pretty_midi.Note(velocity=110, pitch=59, start=note_duration, end=note_duration*2))  # Eb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=note_duration, end=note_duration*2))  # C

# Bar 2: Bb7 (Bb-D-F-A)
# Open voicing: Bb, A, F, D
piano.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar_length + note_duration, end=bar_length + note_duration*2))  # Bb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar_length + note_duration, end=bar_length + note_duration*2))  # A
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar_length + note_duration, end=bar_length + note_duration*2))  # F
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar_length + note_duration, end=bar_length + note_duration*2))  # D

# Bar 3: F7 (F-A-C-Eb)
# Open voicing: F, A, C, Eb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # F
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # A
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # C
piano.notes.append(pretty_midi.Note(velocity=110, pitch=59, start=bar_length*2 + note_duration, end=bar_length*2 + note_duration*2))  # Eb

# Bar 4: C7 (C-E-G-Bb)
# Open voicing: C, Bb, G, E
piano.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # C
piano.notes.append(pretty_midi.Note(velocity=110, pitch=59, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # Bb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # G
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=bar_length*3 + note_duration, end=bar_length*3 + note_duration*2))  # E

# --- SAX: Dante
# One short motif, haunting, incomplete. Start, leave hanging, come back.

# Bar 1: Start of the motif
sax.notes.append(pretty_midi.Note(velocity=105, pitch=66, start=0, end=note_duration))  # F (tenor sax)
sax.notes.append(pretty_midi.Note(velocity=105, pitch=71, start=note_duration*2, end=note_duration*3))  # A
sax.notes.append(pretty_midi.Note(velocity=105, pitch=66, start=note_duration*3, end=note_duration*4))  # F (returns, incomplete)

# Bar 2-4: Leave it hanging. No completion, just space and suggestion.

# Save the MIDI file
pm.save('jazz_intro.mid')
