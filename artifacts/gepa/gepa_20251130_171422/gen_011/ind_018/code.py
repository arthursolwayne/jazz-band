
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Time per bar (1.5 seconds at 160 BPM)
bar_length = 1.5
note_duration = bar_length / 4  # Each beat is 0.375 seconds

# ---------------------------
# Bar 1: Little Ray on Drums (0.0 - 1.5s)
# Tension, groove, no melody — just rhythm to set the mood

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hi-hat on every 8th note
for i in range(8):
    start = i * (note_duration / 2)
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=start + (note_duration / 2)))

# ---------------------------
# Bar 2: Full Quartet (1.5 - 3.0s)

# Saxophone: Melody starts
# Fm7 -> Ab7 -> Bb7 -> Cm7 (Fm key)
# Play a simple but emotional motif: F, Ab, Bb, C (a bluesy turn)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75),  # F (tenor sax)
    pretty_midi.Note(velocity=100, pitch=81, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.5),  # C
]

# Bass: Chromatic walking bass line
# F -> E -> D -> C -> B -> A -> G -> F (chromatic down)
# Each note on beat
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=46, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=70, pitch=45, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=70, pitch=44, start=2.625, end=3.0),  # C
]

# Piano: Comp on offbeats with 7th chords
# Fm7 on beat 1, Ab7 on beat 2, Bb7 on beat 3, Cm7 on beat 4
# Root + 7th, played on offbeats (beat 1.5, 2.5, 3.5, 4.5)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=1.875),  # C (7th)
    
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.375),  # E (7th)
    
    pretty_midi.Note(velocity=90, pitch=52, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=2.875),  # F (7th)
    
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=54, start=3.25, end=3.375),  # B (7th)
]

# Drums: Continue with same pattern
for i in range(8):
    start = 1.5 + i * (note_duration / 2)
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=start + (note_duration / 2)))

# ---------------------------
# Bar 3: Full Quartet (3.0 - 4.5s)
# Saxophone: Repeat the motif, but with slight variation

sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=87, start=3.75, end=4.0),
])

# Bass: Chromatic walking again
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=40, start=4.125, end=4.5),
])

# Piano: Same 7th chords, different placement
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.375),
    
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=3.875),
    
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=58, start=4.25, end=4.375),
    
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=4.875),
])

# Drums: Same pattern
for i in range(8):
    start = 3.0 + i * (note_duration / 2)
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=start + (note_duration / 2)))

# ---------------------------
# Bar 4: Full Quartet (4.5 - 6.0s)
# Saxophone: End the motif with a resolution
# Fm7 -> Cm7, then a final F to resolve

sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=87, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=84, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=84, start=5.25, end=5.5),
])

# Bass: Chromatic walking again
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=39, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=37, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=36, start=5.625, end=6.0),
])

# Piano: Resolve with Cm7 on the final bar
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=4.875),  # C (root)
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=4.875),  # B (7th)
    
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.375),
    
    pretty_midi.Note(velocity=90, pitch=48, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=54, start=5.75, end=5.875),
])

# Drums: Same pattern
for i in range(8):
    start = 4.5 + i * (note_duration / 2)
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=start + (note_duration / 2)))

# Add all notes to their respective instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Save the MIDI file
midi.write("4-bar_intro_Fm.mid")
