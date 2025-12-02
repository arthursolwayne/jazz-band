
import pretty_midi

# Settings
tempo = 160  # BPM
time_signature = (4, 4)
key = 'Dm'  # D minor

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(time_signature[0], time_signature[1], 0, 0))

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Acoustic Drum Set
bass = pretty_midi.Instrument(program=33)    # Electric Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Grand Piano
sax = pretty_midi.Instrument(program=65)    # Tenor Saxophone

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define time in seconds per bar
time_per_bar = 60.0 / tempo * 4  # 4/4 time
time_per_beat = time_per_bar / 4  # 4 beats per bar
time_per_8th = time_per_beat / 2  # 8th notes
time_per_16th = time_per_beat / 4  # 16th notes

# --- DRUMS (Little Ray) - Bar 1: Solo, setup the tension ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 - Time: 0.0 to 1.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=110, pitch=42, start=0.75, end=1.125))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=0.375, end=0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=0.0, end=1.5))     # Hihat on all eighths

# --- BASS (Marcus) - Bar 2-4: Walking line, chromatic approaches, never the same note twice ---
# Dm7 in root position: D, F, A, C
# Walking bass line in Dm7

# Bar 2 - Time: 1.5 to 3.0s
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875))  # D (root)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25)) # D# (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625)) # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0))  # F (3rd)

# Bar 3 - Time: 3.0 to 4.5s
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375))  # G (5th)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75)) # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125)) # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5))  # D

# Bar 4 - Time: 4.5 to 6.0s
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875))  # C (7th)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25)) # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625)) # D#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0))  # E

# --- PIANO (Diane) - Bars 2-4: Comp on 2 and 4 with 7th chords ---
# Dm7 = D, F, A, C
# Comp on 2 and 4 with 7th chords (Dm7 and F7)

# Bar 2 - Time: 1.5 to 3.0s
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25))  # C

# Bar 3 - Time: 3.0 to 4.5s
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75))  # D (F7)

# Bar 4 - Time: 4.5 to 6.0s
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625))  # C

# --- SAX (You) - Bar 2-4: Motif, sing, leave it hanging, return to finish it ---
# Dm7 scale: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - A (sings, resolves to A, then comes back to D)

# Bar 2 - Time: 1.5 to 3.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.6875, end=1.875)) # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25))  # A

# Bar 3 - Time: 3.0 to 4.5s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875))  # A (hold)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.1875, end=3.375)) # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75))  # D

# Bar 4 - Time: 4.5 to 6.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875))  # D (return to start)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.6875, end=4.875)) # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25))  # A

# Write to MIDI file
pm.write('the_cellar_intro.mid')
