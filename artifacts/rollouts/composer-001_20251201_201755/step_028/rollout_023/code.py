
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.125), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875), # D2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.625), # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=4.0), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.375), # F2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # G#2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.125), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.125, end=5.5), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.875), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=5.875, end=6.0), # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=3.0), # E5
    # Bar 3 (3.0 - 4.5s) - G7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5), # G4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5), # B4
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=4.5), # F#5
    # Bar 4 (4.5 - 6.0s) - C7
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0), # C4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=6.0), # E4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0), # G4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0), # B4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Melody starts
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0), # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25), # E4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5), # G4
    # Bar 3 (3.0 - 4.5s) - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5), # A4
    # Bar 4 (4.5 - 6.0s) - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75), # E4
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0), # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5), # A4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0), # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0)
]
# Snare on 2 and 4
snare_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75)
]
# Hi-hat on every eighth
hihat_notes = []
for i in range(3):
    for j in range(8):
        start = 1.5 + i * 1.5 + j * 0.375
        end = start + 0.1875
        hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
