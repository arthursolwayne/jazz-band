
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
    # Hihat on every eighth
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
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # G2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # G2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # E5
]
# Bar 3: Bb7 (Bb D F A)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375)) # Bb4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375)) # D4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)) # F4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375)) # A4
# Bar 4: E7 (E G B D)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)) # E4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)) # G4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)) # B4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)) # D5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0))   # C5 (resolve)
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), A (68), Bb (62), F (65) — then leave it hanging on Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # A4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # Bb4 (hanging)
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0625), # F4 (return)
    pretty_midi.Note(velocity=110, pitch=68, start=5.0625, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625), # F4
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern for bars 2-4
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5 + i * 1.5, note.end + 1.5 + i * 1.5)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
