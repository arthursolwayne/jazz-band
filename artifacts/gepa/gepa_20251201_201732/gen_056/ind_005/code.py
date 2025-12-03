
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2), roots and fifths with chromatic approaches
# D2 = MIDI 38, G2 = MIDI 43
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Root
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # Fifth
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625), # Chromatic approach down
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0), # Root
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0), # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0), # Ab (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0), # C (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0), # Db (MIDI 58)
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, G, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # Root
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # Fifth
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # Chromatic approach up
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5), # Root
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5), # Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5), # D (MIDI 55)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5), # F (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5), # Ab (MIDI 60)
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # Root
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # Fifth
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Chromatic approach down
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Root
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0), # C (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0), # Eb (MIDI 61)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0), # G (MIDI 55)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0), # Bb (MIDI 50)
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
