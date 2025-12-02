
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for i in range(4):  # Four beats per bar
    time = i * 0.375  # 0.375s per beat at 160 BPM
    if i == 0 or i == 2:  # Kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    if i == 1 or i == 3:  # Snare on 2 and 4
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Bar 2: Full band enters
# Start time is 1.5s (Bar 2)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.625),  # D (root)
    pretty_midi.Note(velocity=80, pitch=71, start=1.625, end=1.75), # C (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=1.875),  # Bb (Dm7)
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.0, end=2.125),  # F (Dm7)
    pretty_midi.Note(velocity=80, pitch=73, start=2.125, end=2.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5),  # G (Dm7)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 = D, F, A, C (pitches 72, 74, 76, 71)
# Comp on 2 and 4 (beats 2 and 4 of bar 2)

# Bar 2: beat 2 (1.625s)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=72, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=85, pitch=74, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=76, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=85, pitch=71, start=1.625, end=1.75),  # C
]

# Bar 2: beat 4 (2.0s)
piano_notes += [
    pretty_midi.Note(velocity=85, pitch=72, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=85, pitch=74, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=85, pitch=76, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=85, pitch=71, start=2.0, end=2.125),  # C
]

piano.notes.extend(piano_notes)

# Sax: Your motif — one short phrase, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm in Dorian scale: D, E, F, G, A, B, C
# Motif: D - F - A - G (Dm7 arpeggio with a twist)

# Bar 2: Start the motif on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=75, start=1.875, end=2.0),   # G (leans into Bb)
]

# Bar 3: No sax — leave it hanging
# Bar 4: Come back and finish it
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=75, start=3.875, end=4.0),   # G
]

sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Same pattern for bar 3
for i in range(4):
    time = 1.5 + i * 0.375  # Start of bar 2
    time += 1.5  # Move to bar 3
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    if i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Bar 4: Drums again
for i in range(4):
    time = 1.5 + i * 0.375  # Start of bar 2
    time += 3.0  # Move to bar 4
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    if i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
