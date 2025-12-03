
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2 - G2)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # F#2
    # Bar 3 (G2 - B2)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # C#3
    # Bar 4 (B2 - D3)
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # F3
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),   # E3
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4, open voicings, resolve on the last bar
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C#5
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.5),  # F5
    # Bar 4: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # A5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: A4 (Bb is D), start on beat 1, end on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=2.0),
    # Bar 3: Start again, same motif
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),
    # Bar 4: Continue, finish the motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
# Bar 2
for i in range(0, 6):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25 + i * 0.375, end=2.25 + (i + 1) * 0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))  # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))   # Snare on 2
for i in range(0, 6):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375, end=3.0 + (i + 1) * 0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))   # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)) # Snare on 2
for i in range(0, 6):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125 + i * 0.375, end=4.125 + (i + 1) * 0.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))   # Kick on 1
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # Snare on 2

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
