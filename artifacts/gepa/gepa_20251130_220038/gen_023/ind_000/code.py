
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
drum_notes = [
    (36, 0.0),  # Kick on 1
    (38, 0.5),  # Snare on 2
    (42, 0.0),  # Hihat on 1
    (42, 0.25), # Hihat on &
    (42, 0.5),  # Hihat on 2
    (42, 0.75), # Hihat on &
    (36, 1.0),  # Kick on 3
    (38, 1.5),  # Snare on 4
    (42, 1.0),  # Hihat on 3
    (42, 1.25), # Hihat on &
    (42, 1.5),  # Hihat on 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 1.75),  # D
    (63, 1.75, 2.0),  # Eb
    (64, 2.0, 2.25),  # E
    (65, 2.25, 2.5),  # F
    # Bar 3
    (67, 2.5, 2.75),  # G
    (69, 2.75, 3.0),  # A
    (67, 3.0, 3.25),  # G
    (65, 3.25, 3.5),  # F
    # Bar 4
    (64, 3.5, 3.75),  # E
    (62, 3.75, 4.0),  # D
    (60, 4.0, 4.25),  # C
    (62, 4.25, 4.5),  # D
    # Bar 4 continuation
    (64, 4.5, 4.75),  # E
    (65, 4.75, 5.0),  # F
    (67, 5.0, 5.25),  # G
    (69, 5.25, 5.5),  # A
    (71, 5.5, 5.75),  # B
    (72, 5.75, 6.0),  # C
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 1
    (67, 1.5, 1.75),  # D
    (72, 1.5, 1.75),  # G
    (69, 1.5, 1.75),  # A
    (74, 1.5, 1.75),  # C
    # Bar 2: E7 on beat 3 (chord change)
    (69, 2.0, 2.25),  # E
    (74, 2.0, 2.25),  # B
    (71, 2.0, 2.25),  # C#
    (76, 2.0, 2.25),  # D
    # Bar 3: A7 on beat 1
    (69, 2.5, 2.75),  # A
    (74, 2.5, 2.75),  # D
    (71, 2.5, 2.75),  # E
    (76, 2.5, 2.75),  # F#
    # Bar 3: B7 on beat 3
    (71, 3.0, 3.25),  # B
    (76, 3.0, 3.25),  # E
    (78, 3.0, 3.25),  # F#
    (81, 3.0, 3.25),  # A
    # Bar 4: D7 on beat 1
    (67, 3.5, 3.75),  # D
    (72, 3.5, 3.75),  # G
    (69, 3.5, 3.75),  # A
    (74, 3.5, 3.75),  # C
    # Bar 4: G7 on beat 3
    (67, 4.0, 4.25),  # G
    (72, 4.0, 4.25),  # B
    (69, 4.0, 4.25),  # D
    (74, 4.0, 4.25),  # F
    # Bar 4: C7 on beat 4
    (60, 4.75, 5.0),  # C
    (65, 4.75, 5.0),  # E
    (62, 4.75, 5.0),  # G
    (67, 4.75, 5.0),  # B
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    (67, 1.5, 1.75),  # D (D)
    (72, 1.75, 2.0),  # G (G)
    (74, 2.0, 2.25),  # B (B)
    (67, 2.25, 2.5),  # D (D)
    # Bar 3: Leave it hanging
    (76, 2.5, 2.75),  # F# (F#)
    (74, 2.75, 3.0),  # B (B)
    (67, 3.0, 3.25),  # D (D)
    (65, 3.25, 3.5),  # C (C)
    # Bar 4: Return and finish it
    (72, 3.5, 3.75),  # G (G)
    (74, 3.75, 4.0),  # B (B)
    (67, 4.0, 4.25),  # D (D)
    (62, 4.25, 4.5),  # D (D)
    (67, 4.5, 4.75),  # D (D)
    (69, 4.75, 5.0),  # E (E)
    (67, 5.0, 5.25),  # D (D)
    (64, 5.25, 5.5),  # C (C)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 2
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 0.625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.0, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.625))

    # Hihat on every eighth
    for i in range(0, 8):
        time = start + i * 0.25
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
