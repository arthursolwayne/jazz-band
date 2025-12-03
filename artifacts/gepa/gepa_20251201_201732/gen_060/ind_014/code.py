
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass line: Marcus, walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (MIDI 38), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.0),
    # Bar 3: A (MIDI 43), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    # Bar 4: D (MIDI 38), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=39, start=2.875, end=3.0),
    # Bar 5: A (MIDI 43), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    # Bar 6: D (MIDI 38), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=39, start=3.875, end=4.0),
    # Bar 7: A (MIDI 43), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5),
    # Bar 8: D (MIDI 38), chromatic approach on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (F#-A-C#-D)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # C#
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D
]
# Bar 3: Gm7 (Bb-D-F-G)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=60, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=67, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.0, end=2.25),  # G
])
# Bar 4: C7 (E-G-B-C)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=95, pitch=60, start=2.5, end=2.75),  # C
])
# Bar 5: F#7 (A-C#-E-F#)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),  # C#
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.25),  # F#
])
# Bar 6: Bm7 (D-F#-A-B)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.75),  # B
])
# Bar 7: E7 (G-B-D-E)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=95, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25),  # E
])
# Bar 8: A7 (C#-E-G-A)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # A
])
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (MIDI 62), F# (67), A (69), D (62)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),
]
# Bar 3: Leave it hanging
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),
])
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),
])
# Bar 5: Repeat the motif with variation
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
])
# Bar 6: Leave it hanging again
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),
])
# Bar 7: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
])
# Bar 8: End on a high note
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),
])
sax.notes.extend(sax_notes)

# Drums: continue in bars 2-4
# Bar 2 (1.5-3.0)
for i in range(4):
    # Kick on 1 and 3
    start = 1.5 + i * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    for j in range(2):
        # Kick
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start + j * 1.125, end=kick_end + j * 1.125))
        # Snare
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start + j * 1.125, end=snare_end + j * 1.125))
        # Hihat
        for k in range(8):
            hihat_start = start + j * 1.125 + k * 0.1875
            hihat_end = hihat_start + 0.1875
            drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
