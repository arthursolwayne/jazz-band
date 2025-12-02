
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
    # Bar 1
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 42, 100), # Hihat on &4
    (2.625, 42, 100), # Hihat on &4
    (3.0, 36, 100)   # Kick on 1 (next bar)
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm
bass_notes = [
    (1.5, 62, 100),  # D
    (1.75, 60, 100),  # C
    (2.0, 62, 100),   # D
    (2.25, 64, 100),  # Eb
    (2.5, 67, 100),   # G
    (2.75, 69, 100),  # A
    (3.0, 71, 100),   # Bb
    (3.25, 69, 100),  # A
    (3.5, 67, 100),   # G
    (3.75, 64, 100),  # Eb
    (4.0, 62, 100),   # D
    (4.25, 60, 100),  # C
    (4.5, 62, 100),   # D
    (4.75, 64, 100),  # Eb
    (5.0, 67, 100),   # G
    (5.25, 69, 100),  # A
    (5.5, 71, 100),   # Bb
    (5.75, 69, 100)   # A
]

for time, note, velocity in bass_notes:
    bn = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (1.5, 62, 100),  # D7 (D, F#, A, C)
    (1.75, 64, 100), # Eb
    (2.0, 69, 100),  # A
    (2.25, 67, 100), # G
    (2.5, 62, 100),  # D7
    (2.75, 64, 100), # Eb
    (3.0, 69, 100),  # A
    (3.25, 67, 100), # G
    (3.5, 62, 100),  # D7
    (3.75, 64, 100), # Eb
    (4.0, 69, 100),  # A
    (4.25, 67, 100), # G
    (4.5, 62, 100),  # D7
    (4.75, 64, 100), # Eb
    (5.0, 69, 100),  # A
    (5.25, 67, 100), # G
    (5.5, 62, 100),  # D7
    (5.75, 64, 100)  # Eb
]

for time, note, velocity in piano_notes:
    pn = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_continued = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (1.75, 38, 100), # Snare on 2
    (2.0, 42, 100),  # Hihat on &2
    (2.25, 42, 100), # Hihat on &3
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &4
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (3.75, 38, 100), # Snare on 2
    (4.0, 42, 100),  # Hihat on &2
    (4.25, 42, 100), # Hihat on &3
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &4
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
    # Bar 4
    (5.5, 36, 100),  # Kick on 1
    (5.75, 38, 100), # Snare on 2
    (6.0, 42, 100),  # Hihat on &2
    (6.25, 42, 100), # Hihat on &3
    (6.5, 36, 100),  # Kick on 3
    (6.75, 42, 100), # Hihat on &4
    (7.0, 38, 100),  # Snare on 4
    (7.25, 42, 100)  # Hihat on &4
]

for time, note, velocity in drum_notes_continued:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Dante: Tenor sax — one short motif, make it sing
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 64, 100), # Eb
    (2.0, 67, 100),  # G
    (2.25, 69, 100), # A
    (2.5, 67, 100),  # G
    (2.75, 71, 100), # Bb
    (3.0, 69, 100),  # A
    (3.25, 67, 100), # G
    (3.5, 64, 100),  # Eb
    (3.75, 62, 100), # D
    (4.0, 62, 100),  # D
    (4.25, 64, 100), # Eb
    (4.5, 67, 100),  # G
    (4.75, 69, 100), # A
    (5.0, 67, 100),  # G
    (5.25, 71, 100), # Bb
    (5.5, 69, 100),  # A
    (5.75, 67, 100)  # G
]

for time, note, velocity in sax_notes:
    sn = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
