
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.1875, 0.1875),  # Hihat on 1&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),  # Hihat on 2&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.9375, 0.1875),  # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (40, 1.875, 0.375),  # F on 2
    (43, 2.25, 0.375),  # A on 3
    (41, 2.625, 0.375),  # G on 4
    (37, 2.625, 0.375),  # C on 4 (chromatic approach)
    (38, 3.0, 0.375),  # D2 on 1
    (40, 3.375, 0.375),  # F on 2
    (43, 3.75, 0.375),  # A on 3
    (41, 4.125, 0.375),  # G on 4
    (37, 4.125, 0.375),  # C on 4 (chromatic approach)
    (38, 4.5, 0.375),  # D2 on 1
    (40, 4.875, 0.375),  # F on 2
    (42, 5.25, 0.375),  # Bb on 3
    (41, 5.625, 0.375)  # G on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (62, 1.5, 0.5),  # D
    (64, 1.5, 0.5),  # F
    (67, 1.5, 0.5),  # A
    (69, 1.5, 0.5),  # C
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    (67, 2.25, 0.5),  # G
    (69, 2.25, 0.5),  # B
    (71, 2.25, 0.5),  # D
    (74, 2.25, 0.5),  # F
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    (60, 3.0, 0.5),  # C
    (62, 3.0, 0.5),  # Eb
    (67, 3.0, 0.5),  # G
    (69, 3.0, 0.5),  # Bb
])
# Add resolving note on beat 4 of each bar
piano_notes.extend([
    (64, 1.5, 0.5),  # F on beat 4 of bar 2
    (71, 2.25, 0.5),  # D on beat 4 of bar 3
    (69, 3.0, 0.5),  # Bb on beat 4 of bar 4
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    (62, 1.5, 0.375),  # D (beat 1)
    (64, 1.875, 0.375),  # Eb (beat 2)
    (64, 2.25, 0.375),  # Eb (beat 3)
    (67, 2.625, 0.375),  # G (beat 4)
    (67, 3.0, 0.375),  # G (beat 1)
    (69, 3.375, 0.375),  # A (beat 2)
    (69, 3.75, 0.375),  # A (beat 3)
    (62, 4.125, 0.375)   # D (beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.6875, 0.1875),  # Hihat on 1&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 2.0625, 0.1875),  # Hihat on 2&
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.4375, 0.1875),  # Hihat on 3&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.8125, 0.1875),  # Hihat on 4&
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.1875, 0.1875),  # Hihat on 1&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.5625, 0.1875),  # Hihat on 2&
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.9375, 0.1875),  # Hihat on 3&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.3125, 0.1875),  # Hihat on 4&
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.6875, 0.1875),  # Hihat on 1&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 5.0625, 0.1875),  # Hihat on 2&
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.4375, 0.1875),  # Hihat on 3&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.8125, 0.1875)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
