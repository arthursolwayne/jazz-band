
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds
KICK = 36
SNARE = 38
HIHAT = 42

# Time structure (in seconds)
BAR_DURATION = 1.5  # 160 BPM, 4/4 time
BAR_1_START = 0.0
BAR_1_END = BAR_DURATION
BAR_2_START = BAR_1_END
BAR_4_END = BAR_1_END + 3 * BAR_DURATION

# --------------------------- DRUMS (Bar 1: 0.0 - 1.5s) ---------------------------

# Bar 1: Little Ray alone — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 1st beat: 0.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
# 2nd beat: 0.375s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
# 3rd beat: 0.75s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))
# 4th beat: 1.125s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))
# Hi-hats every eighth note
for i in range(8):
    start = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=start + 0.375))

# --------------------------- PIANO (Bar 2-4: 1.5 - 6.0s) ---------------------------

# Diane's piano: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2 (1.5 - 3.0s)
# Dm7 (D, F, A, C) on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # C

# Bar 3 (3.0 - 4.5s)
# Dm7 on beat 2 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))  # C

# Bar 4 (4.5 - 6.0s)
# Dm7 on beat 2 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625))  # C

# --------------------------- BASS (Bar 2-4: 1.5 - 6.0s) ---------------------------

# Marcus's bass: walking line, chromatic approaches, no repeated notes

# Bar 2: C - D - Eb - F (chromatic lead into Dm)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0))   # F

# Bar 3: F - G - Ab - Bb (chromatic lead into Dm)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125))  # Ab
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5))   # Bb

# Bar 4: Bb - C - D - Eb (chromatic lead out from Dm)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875))   # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25))  # C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0))   # Eb

# --------------------------- SAX (Bar 2-4: 1.5 - 6.0s) ---------------------------

# Dante's sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: D - Eb - F - G (4 notes), spaced out
# Bar 2: Start it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))   # G

# Bar 3: Leave it hanging (rest)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # D (return to motif)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # F

# Bar 4: Finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875))  # G

# --------------------------- Add instruments to MIDI ---------------------------
midi.instruments.extend([sax, bass, piano, drums])

# Save as MIDI file
midi.write("dante_intro.mid")
