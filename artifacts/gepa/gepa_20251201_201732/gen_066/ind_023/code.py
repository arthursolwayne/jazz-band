
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar (160 BPM, 4/4 time)
BAR_DURATION = 1.5
TIME_PER_BEAT = 0.375  # 160 BPM = 60 / 160 = 0.375 seconds per beat

# Bar 1: Drums only (0.0 - 1.5s)
# Fill the bar with a groove: kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every 8th note
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in D minor (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0))  # C4

# Sax: Motif — short, singable, leaves it hanging
# D (62) - F (65) - Bb (66) - D (62)
# Start at 1.5s, end at 2.25s, leave it hanging until 3.0s

sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0))   # D4 (resolution)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Dm7 to Gm7 (D2 -> G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),   # C3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5))  # F4

# Sax: Continue motif — repeat or twist
# Keep the same pattern, but end on a different note (F4 instead of D4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5))   # F4

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Gm7 to Cm7 (G2 -> C2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0))  # Bb4

# Sax: Finish the motif — repeat the first phrase, resolve on C4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0))   # C4

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
