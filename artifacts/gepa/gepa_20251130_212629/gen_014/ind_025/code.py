
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Function to convert time (in seconds) to ticks
def to_ticks(t):
    return int(t * midi.time_signature_numerator / midi.time_signature_denominator * midi.resolution)

#-------------------
# Bar 1: Little Ray on drums (0.0 - 1.5s)
#-------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar is 1.5 seconds long, 4 beats at 160 BPM (beat = 0.375s)
for beat in [0, 2]:  # Kick on 1 and 3
    note = pretty_midi.Note(
        velocity=100,
        pitch=kick,
        start=beat * 0.375,
        end=beat * 0.375 + 0.1
    )
    drums.notes.append(note)

for beat in [1, 3]:  # Snare on 2 and 4
    note = pretty_midi.Note(
        velocity=90,
        pitch=snare,
        start=beat * 0.375,
        end=beat * 0.375 + 0.1
    )
    drums.notes.append(note)

# Hihat on every eighth note
for i in range(8):
    note = pretty_midi.Note(
        velocity=70,
        pitch=hihat,
        start=i * 0.1875,
        end=i * 0.1875 + 0.05
    )
    drums.notes.append(note)

#-------------------
# Bar 2-3: Full Quartet (1.5 - 4.5s)
#-------------------

#-------------------
# Bass Line (Marcus) - Walking line in Dm
# Dm7: D, F, A, C
# Chromatic approach on beat 3 of bar 2
#-------------------

bass_notes = [
    # Bar 2: Dm7, chromatic approach to D
    pretty_midi.Note(velocity=75, pitch=62, start=1.5, end=1.5 + 0.375),  # C (chromatic approach)
    pretty_midi.Note(velocity=75, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75),  # D
    pretty_midi.Note(velocity=75, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125),  # F
    pretty_midi.Note(velocity=75, pitch=69, start=1.5 + 1.125, end=1.5 + 1.5),  # A

    # Bar 3: Dm7, chromatic approach to F
    pretty_midi.Note(velocity=75, pitch=65, start=1.5 + 1.5, end=1.5 + 1.875),  # E (chromatic approach)
    pretty_midi.Note(velocity=75, pitch=67, start=1.5 + 1.875, end=1.5 + 2.25),  # F
    pretty_midi.Note(velocity=75, pitch=69, start=1.5 + 2.25, end=1.5 + 2.625),  # A
    pretty_midi.Note(velocity=75, pitch=71, start=1.5 + 2.625, end=1.5 + 3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

#-------------------
# Piano (Diane) - Comping on 2 and 4, 7th chords
#-------------------

# Dm7 = D, F, A, C
# Comp on beats 2 and 4 (0.75 and 1.5 seconds into bar 2, etc.)
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5 + 0.75, end=1.5 + 0.75 + 0.1),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 0.75, end=1.5 + 0.75 + 0.1),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5 + 0.75, end=1.5 + 0.75 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5 + 0.75, end=1.5 + 0.75 + 0.1),  # A
    # Bar 2, beat 4
    pretty_midi.Note(velocity=85, pitch=62, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1),  # A
    # Bar 3, beat 2 (2.25 into the bar = 3.75 total)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5 + 2.25, end=1.5 + 2.25 + 0.1),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 2.25, end=1.5 + 2.25 + 0.1),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5 + 2.25, end=1.5 + 2.25 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5 + 2.25, end=1.5 + 2.25 + 0.1),  # A
    # Bar 3, beat 4 (3.0 into the bar = 4.5 total)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5 + 3.0, end=1.5 + 3.0 + 0.1),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=1.5 + 3.0, end=1.5 + 3.0 + 0.1),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5 + 3.0, end=1.5 + 3.0 + 0.1),  # A
]

for note in piano_notes:
    piano.notes.append(note)

#-------------------
# Sax (Dante) - Motif, slow and deliberate, in Dm
# Motif: D -> F -> Bb -> A (chromatic into Dm)
# Play it on the first two beats of bar 2, leave it hanging, come back at bar 3
#-------------------

# Bar 2: First two beats (1.5 - 2.25s)
note1 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375)  # D
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75)  # F
note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)  # A
note4 = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.125, end=1.5 + 1.5)  # C

# Bar 3: Finish the motif on beat 3 (2.625 into the bar = 4.125 total)
note5 = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2.625, end=1.5 + 3.0)  # D

# Add notes to sax instrument
sax.notes.extend([note1, note2, note3, note4, note5])

#-------------------
# Add instruments to MIDI
#-------------------
midi.instruments.extend([sax, bass, piano, drums])

#-------------------
# Save the MIDI file
#-------------------
midi.write("dante_intro.mid")
