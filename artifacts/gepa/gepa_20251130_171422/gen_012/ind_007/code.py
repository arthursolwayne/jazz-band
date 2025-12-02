
import pretty_midi

# Create the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums - MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration in seconds (160 BPM, 4/4 time)
bar_duration = 1.5  # 60 / 160 * 4 = 1.5

# ---------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Only drums in this bar

# Create drum notes
drum_notes = []

# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every eighth
for i in range(0, 6):
    start = i * 0.375
    end = start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

# Add to drums instrument
for note in drum_notes:
    drums.notes.append(note)

# ---------------------
# Bars 2-4: Full quartet (1.5 - 6.0s)

# ---------------------
# Bass: Marcus - walking line, chromatic approaches, no repeats
# Fm7 = F, Ab, Bb, D
# Start on Bb (chromatic approach to F)

bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875))  # Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25))  # A
bass_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625))  # G
bass_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0))  # Gb (chromatic)

bass_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375))  # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75))  # Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125))  # A
bass_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5))  # G

bass_notes.append(pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875))  # Gb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25))  # F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625))  # Bb
bass_notes.append(pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0))  # A

for note in bass_notes:
    bass.notes.append(note)

# ---------------------
# Piano: Diane - 7th chords, comp on 2 and 4, let the space breathe

# Fm7 = F, Ab, Bb, D
# D7 = D, F#, A, C
# Bb7 = Bb, Db, F, Ab

piano_notes = []

# Bar 2 (1.5 - 3.0)
# Fm7: F, Ab, Bb, D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875))  # Ab
piano_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875))  # Bb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=56, start=1.5, end=1.875))  # D

# Bar 3 (3.0 - 4.5)
# D7: D, F#, A, C
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375))  # D
piano_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375))  # F#
piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375))  # A
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375))  # C

# Bar 4 (4.5 - 6.0)
# Bb7: Bb, Db, F, Ab
piano_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875))  # Bb
piano_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875))  # Db
piano_notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875))  # F
piano_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875))  # Ab

for note in piano_notes:
    piano.notes.append(note)

# ---------------------
# Sax: Dante - one short motif, make it sing, leave it hanging, come back

# Motif: F, Ab, Bb, D (Fm7)
# Start at 1.5, end at 2.0
# Then wait, come back at 4.0 to finish

sax_notes = []

# First phrase: F, Ab, Bb, D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75))  # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0))  # Ab

# Leave it hanging for a moment
# Come back at 4.0 to finish the motif

sax_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25))  # Bb
sax_notes.append(pretty_midi.Note(velocity=100, pitch=56, start=4.25, end=4.5))  # D

for note in sax_notes:
    sax.notes.append(note)

# ---------------------
# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_4_bar_intro.mid")
