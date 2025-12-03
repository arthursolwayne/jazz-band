
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # D2 (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # F3 (root octave)
    
    # Bar 3: Ab7 (Ab, Db, G, F)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Ab2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # C3 (root octave)
    
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # D2 (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),  # F3 (root octave)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
]

# Bar 3: Ab7 (Ab, Db, G, F)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))  # Ab4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5))  # Db4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5))  # G5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5))  # F4

# Bar 4: Dm7 (D, F, A, C)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # D4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0))  # F4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0))  # A5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0))  # C4)
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, D5, C4 (Fm7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # C4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # F4 (reprise)
    pretty_midi.Note(velocity=110, pitch=61, start=3.375, end=3.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),   # C4
    # End with a slight resolution
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # D5 (fifth)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),   # C4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)

# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
