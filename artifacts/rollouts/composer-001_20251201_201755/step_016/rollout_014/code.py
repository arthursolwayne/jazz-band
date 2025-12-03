
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # Bb2 (root of next chord)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # D2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),  # Eb2 (root of next chord)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Ab2 (root of next chord)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # E4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=85, pitch=68, start=3.0, end=3.375),  # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),  # D4
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) – Bb (68) – F (65) – G (67)
# Start on beat 2 of bar 2, then leave it hanging on beat 4, resolve at the start of bar 3
# Then repeat with variation on beat 2 of bar 4
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G4

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),   # F4
]
sax.notes.extend(sax_notes)

# Drums (Bar 2-4): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in [0, 2]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.75, end=1.5 + i*0.75 + 0.375))
for i in [1, 3]:
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*0.75, end=1.5 + i*0.75 + 0.125))
for i in range(8):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.1875, end=1.5 + i*0.1875 + 0.1875))

# Bar 3 (3.0 - 4.5s)
for i in [0, 2]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*0.75, end=3.0 + i*0.75 + 0.375))
for i in [1, 3]:
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0 + i*0.75, end=3.0 + i*0.75 + 0.125))
for i in range(8):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.1875, end=3.0 + i*0.1875 + 0.1875))

# Bar 4 (4.5 - 6.0s)
for i in [0, 2]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*0.75, end=4.5 + i*0.75 + 0.375))
for i in [1, 3]:
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.5 + i*0.75, end=4.5 + i*0.75 + 0.125))
for i in range(8):
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.1875, end=4.5 + i*0.1875 + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
