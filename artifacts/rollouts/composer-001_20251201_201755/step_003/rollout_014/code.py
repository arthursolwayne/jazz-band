
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
time = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5))

# Hihat on every eighth
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
time = 1.5

# Bass: D2 (MIDI 38), G2 (MIDI 43), chromatic approach on D2
# Bar 2: D2 -> Eb2 -> D2 -> G2 (MIDI: 38 -> 39 -> 38 -> 43)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time + 0.375, end=time + 0.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time + 0.75, end=time + 1.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time + 1.125, end=time + 1.5))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.75))  # F#4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.75))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time, end=time + 0.75))  # C#4

# Sax: Start the motif
# D4 -> F#4 -> E4 -> D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=time + 0.375, end=time + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=time + 0.75, end=time + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time + 1.125, end=time + 1.5))

# Bar 3: Full quartet (3.0 - 4.5s)
time = 3.0

# Bass: G2 (MIDI 43), A2 (MIDI 44), chromatic approach on G2
# Bar 3: G2 -> Ab2 -> G2 -> D3 (MIDI: 43 -> 44 -> 43 -> 50)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time, end=time + 0.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=time + 0.375, end=time + 0.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time + 0.75, end=time + 1.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=time + 1.125, end=time + 1.5))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.75))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.75))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=time, end=time + 0.75))  # F4

# Sax: Continue the motif (reprise)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=time + 0.375, end=time + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=time + 0.75, end=time + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=time + 1.125, end=time + 1.5))

# Bar 4: Full quartet (4.5 - 6.0s)
time = 4.5

# Bass: D2 (MIDI 38), E2 (MIDI 40), chromatic approach on D2
# Bar 4: D2 -> Eb2 -> D2 -> D3 (MIDI: 38 -> 39 -> 38 -> 50)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time + 0.375, end=time + 0.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time + 0.75, end=time + 1.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=time + 1.125, end=time + 1.5))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D, F#, A, C#) – resolves to D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.75))  # F#4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.75))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=time, end=time + 0.75))  # C#4

# Sax: Finish the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=time + 0.375, end=time + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=time + 0.75, end=time + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time + 1.125, end=time + 1.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2, 3, 4: same pattern
for bar in range(2, 5):
    time = bar * bar_length
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5))

    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
