
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
    (36, 0.0, 0.375),  # Kick on beat 1
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875) # Hihat on &
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line in D, with root on beat 1
bass_notes = [
    (50, 1.5, 1.5), # D on beat 1 of bar 2
    (51, 1.875, 1.875), # Eb on &
    (52, 2.25, 2.25), # E on beat 2
    (53, 2.625, 2.625), # F on &
    (55, 3.0, 3.0), # G on beat 3
    (56, 3.375, 3.375), # Ab on &
    (57, 3.75, 3.75), # A on beat 4
    (58, 4.125, 4.125), # Bb on &
    (62, 4.5, 4.5), # C on beat 1 of bar 3
    (63, 4.875, 4.875), # C# on &
    (64, 5.25, 5.25), # D on beat 2
    (65, 5.625, 5.625), # Eb on &
    (67, 6.0, 6.0), # F on beat 1 of bar 4
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano chords - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 1.5), # C7 root
    (64, 1.5, 1.5), # E7
    (67, 1.5, 1.5), # G7
    (71, 1.5, 1.5), # B7
    (64, 2.25, 2.25), # E7 on beat 2
    (67, 2.25, 2.25), # G7
    (71, 2.25, 2.25), # B7
    (74, 2.25, 2.25), # D7
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 3.0), # C7 root
    (64, 3.0, 3.0), # E7
    (67, 3.0, 3.0), # G7
    (71, 3.0, 3.0), # B7
    (64, 3.75, 3.75), # E7 on beat 2
    (67, 3.75, 3.75), # G7
    (71, 3.75, 3.75), # B7
    (74, 3.75, 3.75), # D7
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 4.5), # C7 root
    (64, 4.5, 4.5), # E7
    (67, 4.5, 4.5), # G7
    (71, 4.5, 4.5), # B7
    (64, 5.25, 5.25), # E7 on beat 2
    (67, 5.25, 5.25), # G7
    (71, 5.25, 5.25), # B7
    (74, 5.25, 5.25), # D7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax melody - concise, emotional motif in D
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    (62, 1.5, 1.6875), # D
    (64, 1.6875, 1.875), # E
    (65, 1.875, 2.0625), # F
    (62, 2.0625, 2.25), # D
    # Bar 3 (3.0 - 4.5s)
    (67, 3.0, 3.1875), # G
    (69, 3.1875, 3.375), # A
    (67, 3.375, 3.5625), # G
    (64, 3.5625, 3.75), # E
    # Bar 4 (4.5 - 6.0s)
    (69, 4.5, 4.6875), # A
    (71, 4.6875, 4.875), # B
    (67, 4.875, 5.0625), # G
    (64, 5.0625, 5.25), # E
    (62, 5.25, 5.4375), # D
    (62, 5.4375, 5.625), # D
    (62, 5.625, 5.8125), # D
    (62, 5.8125, 6.0), # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
