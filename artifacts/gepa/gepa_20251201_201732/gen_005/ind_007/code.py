
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
for bar in range(1):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane on piano, open voicings
# Bar 2 chord: Fmaj7 (F, A, C, E)
# Bar 3 chord: G7 (G, B, D, F)
# Bar 4 chord: Am7 (A, C, E, G)
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    end = start + 1.5
    # Diane: Comp on 2 and 4
    if bar % 2 == 0:
        # Bar 2: Fmaj7 (F, A, C, E)
        if bar == 2:
            notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=end),  # F4
                     pretty_midi.Note(velocity=100, pitch=76, start=start, end=end),  # A4
                     pretty_midi.Note(velocity=100, pitch=72, start=start, end=end),  # C4?
                     pretty_midi.Note(velocity=100, pitch=77, start=start, end=end)]  # E5?
            # Adjust pitches
            notes[0].pitch = 71  # F4
            notes[1].pitch = 76  # A4
            notes[2].pitch = 69  # C4
            notes[3].pitch = 82  # E5
        elif bar == 3:
            notes = [pretty_midi.Note(velocity=100, pitch=78, start=start, end=end),  # G4
                     pretty_midi.Note(velocity=100, pitch=80, start=start, end=end),  # B4
                     pretty_midi.Note(velocity=100, pitch=71, start=start, end=end),  # D4?
                     pretty_midi.Note(velocity=100, pitch=76, start=start, end=end)]  # F4?
            # Adjust pitches
            notes[0].pitch = 78  # G4
            notes[1].pitch = 80  # B4
            notes[2].pitch = 67  # D4
            notes[3].pitch = 76  # F4
        elif bar == 4:
            notes = [pretty_midi.Note(velocity=100, pitch=77, start=start, end=end),  # A4
                     pretty_midi.Note(velocity=100, pitch=72, start=start, end=end),  # C4
                     pretty_midi.Note(velocity=100, pitch=69, start=start, end=end),  # E4?
                     pretty_midi.Note(velocity=100, pitch=82, start=start, end=end)]  # G5?
            # Adjust pitches
            notes[0].pitch = 77  # A4
            notes[1].pitch = 72  # C4
            notes[2].pitch = 69  # E4
            notes[3].pitch = 82  # G5
        for note in notes:
            piano.notes.append(note)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    end = start + 1.5
    time = start
    # Bar 2: F - G - A - Bb (roots and fifths with chromatic approaches)
    bass_notes = [
        pretty_midi.Note(velocity=100, pitch=46, start=time, end=time + 0.375),  # F2
        pretty_midi.Note(velocity=100, pitch=48, start=time + 0.375, end=time + 0.75),  # G2
        pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 1.125),  # A2
        pretty_midi.Note(velocity=100, pitch=51, start=time + 1.125, end=time + 1.5),  # Bb2
    ]
    # Bar 3: G - A - Bb - B
    if bar == 3:
        bass_notes = [
            pretty_midi.Note(velocity=100, pitch=48, start=time, end=time + 0.375),  # G2
            pretty_midi.Note(velocity=100, pitch=50, start=time + 0.375, end=time + 0.75),  # A2
            pretty_midi.Note(velocity=100, pitch=51, start=time + 0.75, end=time + 1.125),  # Bb2
            pretty_midi.Note(velocity=100, pitch=53, start=time + 1.125, end=time + 1.5),  # B2
        ]
    # Bar 4: A - Bb - B - C
    if bar == 4:
        bass_notes = [
            pretty_midi.Note(velocity=100, pitch=50, start=time, end=time + 0.375),  # A2
            pretty_midi.Note(velocity=100, pitch=51, start=time + 0.375, end=time + 0.75),  # Bb2
            pretty_midi.Note(velocity=100, pitch=53, start=time + 0.75, end=time + 1.125),  # B2
            pretty_midi.Note(velocity=100, pitch=55, start=time + 1.125, end=time + 1.5),  # C2
        ]
    for note in bass_notes:
        bass.notes.append(note)

# Dante: Melody in bar 2 (start on F, play a short motif, leave it hanging)
# Motif: F - G - Ab - Bb (fingering: 1, 2, 3, 4)
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    end = start + 1.5
    time = start
    # Bar 2: Play the motif
    sax_notes = [
        pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375),  # F4
        pretty_midi.Note(velocity=110, pitch=72, start=time + 0.375, end=time + 0.75),  # G4
        pretty_midi.Note(velocity=110, pitch=70, start=time + 0.75, end=time + 1.125),  # Ab4
        pretty_midi.Note(velocity=110, pitch=69, start=time + 1.125, end=time + 1.5),  # Bb4
    ]
    # Bar 3: Rest
    if bar == 3:
        sax_notes = []
    # Bar 4: Repeat the motif with resolution to C
    if bar == 4:
        sax_notes = [
            pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375),  # F4
            pretty_midi.Note(velocity=110, pitch=72, start=time + 0.375, end=time + 0.75),  # G4
            pretty_midi.Note(velocity=110, pitch=70, start=time + 0.75, end=time + 1.125),  # Ab4
            pretty_midi.Note(velocity=110, pitch=69, start=time + 1.125, end=time + 1.5),  # Bb4
        ]
        # Add resolution to C (C5)
        sax_notes.append(pretty_midi.Note(velocity=110, pitch=84, start=time + 1.125, end=time + 1.5))
    for note in sax_notes:
        sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    end = start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_russo.mid")
