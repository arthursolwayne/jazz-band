
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: C E♭ G (C4, E♭4, G4) with a half note on C, quarter on E♭, eighth on G
sax_notes = [
    (60, 1.5, 1.0),  # C4 for 1 beat
    (63, 1.5, 0.5),  # E♭4 for 0.5 beats
    (67, 2.0, 0.25)  # G4 for 0.25 beats
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Marcus: Walking bass line in C
# C - B♭ - B - C - D - C - E♭ - D - E - F - G - F - G - A - G - C
bass_notes = [
    (60, 1.5, 0.25), (62, 1.75, 0.25), (63, 2.0, 0.25),
    (60, 2.25, 0.25), (62, 2.5, 0.25), (60, 2.75, 0.25),
    (63, 3.0, 0.25), (62, 3.25, 0.25), (64, 3.5, 0.25),
    (65, 3.75, 0.25), (67, 4.0, 0.25), (65, 4.25, 0.25),
    (67, 4.5, 0.25), (69, 4.75, 0.25), (67, 5.0, 0.25),
    (60, 5.25, 0.25)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: C7 on beat 2, E♭7 on beat 4
piano_notes = [
    (60, 2.0, 0.25), (64, 2.0, 0.25), (67, 2.0, 0.25), (71, 2.0, 0.25),  # C7
    (63, 3.0, 0.25), (67, 3.0, 0.25), (71, 3.0, 0.25), (75, 3.0, 0.25)   # E♭7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: Repeat and vary slightly
sax_notes = [
    (60, 3.0, 1.0),  # C4 for 1 beat
    (63, 3.0, 0.5),  # E♭4 for 0.5 beats
    (67, 3.5, 0.25)  # G4 for 0.25 beats
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Marcus: Walking bass line
# C - B♭ - B - C - D - C - E♭ - D - E - F - G - F - G - A - G - C
bass_notes = [
    (60, 3.0, 0.25), (62, 3.25, 0.25), (63, 3.5, 0.25),
    (60, 3.75, 0.25), (62, 4.0, 0.25), (60, 4.25, 0.25),
    (63, 4.5, 0.25), (62, 4.75, 0.25), (64, 5.0, 0.25),
    (65, 5.25, 0.25), (67, 5.5, 0.25), (65, 5.75, 0.25),
    (67, 6.0, 0.25), (69, 6.25, 0.25), (67, 6.5, 0.25),
    (60, 6.75, 0.25)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
# Bar 3: C7 on beat 2, E♭7 on beat 4
piano_notes = [
    (60, 3.5, 0.25), (64, 3.5, 0.25), (67, 3.5, 0.25), (71, 3.5, 0.25),  # C7
    (63, 4.5, 0.25), (67, 4.5, 0.25), (71, 4.5, 0.25), (75, 4.5, 0.25)   # E♭7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a descending line (G - E♭ - C)
sax_notes = [
    (67, 4.5, 0.25),  # G4
    (63, 4.75, 0.25),  # E♭4
    (60, 5.0, 0.25)    # C4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Marcus: Walking bass line
# C - B♭ - B - C - D - C - E♭ - D - E - F - G - F - G - A - G - C
bass_notes = [
    (60, 4.5, 0.25), (62, 4.75, 0.25), (63, 5.0, 0.25),
    (60, 5.25, 0.25), (62, 5.5, 0.25), (60, 5.75, 0.25),
    (63, 6.0, 0.25), (62, 6.25, 0.25), (64, 6.5, 0.25),
    (65, 6.75, 0.25), (67, 7.0, 0.25), (65, 7.25, 0.25),
    (67, 7.5, 0.25), (69, 7.75, 0.25), (67, 8.0, 0.25),
    (60, 8.25, 0.25)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
# Bar 4: C7 on beat 2, E♭7 on beat 4
piano_notes = [
    (60, 5.0, 0.25), (64, 5.0, 0.25), (67, 5.0, 0.25), (71, 5.0, 0.25),  # C7
    (63, 6.0, 0.25), (67, 6.0, 0.25), (71, 6.0, 0.25), (75, 6.0, 0.25)   # E♭7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
