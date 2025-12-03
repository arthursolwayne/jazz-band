
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
    (36, 0.0, 1.0),  # Kick on beat 1
    (42, 0.125, 0.25),  # Hihat on 1&
    (38, 0.5, 1.0),  # Snare on beat 2
    (42, 0.625, 0.75),  # Hihat on 2&
    (36, 1.0, 1.5),  # Kick on beat 3
    (42, 1.125, 1.25),  # Hihat on 3&
    (38, 1.5, 1.5),  # Snare on beat 4
    (42, 1.625, 1.75),  # Hihat on 4&
]
for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 1.75),  # D2 on beat 1
    (40, 1.75, 2.0),  # Eb2 on 1&
    (43, 2.0, 2.25),  # G2 on beat 2
    (41, 2.25, 2.5),  # Ab2 on 2&
    (38, 2.5, 2.75),  # D2 on beat 3
    (40, 2.75, 3.0),  # Eb2 on 3&
    (43, 3.0, 3.25),  # G2 on beat 4
    (41, 3.25, 3.5),  # Ab2 on 4&
    (38, 3.5, 3.75),  # D2 on beat 1
    (40, 3.75, 4.0),  # Eb2 on 1&
    (43, 4.0, 4.25),  # G2 on beat 2
    (41, 4.25, 4.5),  # Ab2 on 2&
    (38, 4.5, 4.75),  # D2 on beat 3
    (40, 4.75, 5.0),  # Eb2 on 3&
    (43, 5.0, 5.25),  # G2 on beat 4
    (41, 5.25, 5.5),  # Ab2 on 4&
]
for note, start, end in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(bn)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    (62, 1.5, 1.75),  # D4
    (64, 1.5, 1.75),  # F#4
    (67, 1.5, 1.75),  # A4
    (69, 1.5, 1.75),  # C5
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    (67, 2.5, 2.75),  # G4
    (69, 2.5, 2.75),  # B4
    (72, 2.5, 2.75),  # D5
    (71, 2.5, 2.75),  # F5
])
# Bar 4: C7 (C-E-G-B)
piano_notes.extend([
    (60, 3.5, 3.75),  # C4
    (64, 3.5, 3.75),  # E4
    (67, 3.5, 3.75),  # G4
    (71, 3.5, 3.75),  # B4
])
for note, start, end in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(pn)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75),  # Kick on beat 1
    (42, 1.625, 1.75),  # Hihat on 1&
    (38, 2.0, 2.25),  # Snare on beat 2
    (42, 2.125, 2.25),  # Hihat on 2&
    (36, 2.5, 2.75),  # Kick on beat 3
    (42, 2.625, 2.75),  # Hihat on 3&
    (38, 3.0, 3.25),  # Snare on beat 4
    (42, 3.125, 3.25),  # Hihat on 4&
    # Bar 3
    (36, 3.5, 3.75),  # Kick on beat 1
    (42, 3.625, 3.75),  # Hihat on 1&
    (38, 4.0, 4.25),  # Snare on beat 2
    (42, 4.125, 4.25),  # Hihat on 2&
    (36, 4.5, 4.75),  # Kick on beat 3
    (42, 4.625, 4.75),  # Hihat on 3&
    (38, 5.0, 5.25),  # Snare on beat 4
    (42, 5.125, 5.25),  # Hihat on 4&
]
for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Sax: Melody (One short motif, make it sing)
# Bars 2-4: Start it, leave it hanging, come back and finish it
# D4 (62), E4 (64), F#4 (66), A4 (69)
sax_notes = [
    (62, 1.5, 1.75),  # D4 on beat 1
    (64, 1.75, 2.0),  # E4 on 1&
    (66, 2.0, 2.25),  # F#4 on beat 2
    (69, 2.25, 2.5),  # A4 on 2&
    (69, 2.5, 2.75),  # A4 on beat 3
    (66, 2.75, 3.0),  # F#4 on 3&
    (64, 3.0, 3.25),  # E4 on beat 4
    (62, 3.25, 3.5),  # D4 on 4&
    (62, 3.5, 3.75),  # D4 on beat 1
    (64, 3.75, 4.0),  # E4 on 1&
    (66, 4.0, 4.25),  # F#4 on beat 2
    (69, 4.25, 4.5),  # A4 on 2&
    (69, 4.5, 4.75),  # A4 on beat 3
    (66, 4.75, 5.0),  # F#4 on 3&
    (64, 5.0, 5.25),  # E4 on 4&
    (62, 5.25, 5.5),  # D4 on 4&
]
for note, start, end in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
