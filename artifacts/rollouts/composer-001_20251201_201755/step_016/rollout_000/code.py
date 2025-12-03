
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.25),  # C#4
]
# Bar 3: G7 (G-B-D-F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # F4
]
# Bar 4: D7 (D-F#-A-C)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # C4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth (Bars 2-4)
def add_drums(start_time):
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.5, end=start_time + 1.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 2.25, end=start_time + 2.625)
    hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.5, end=start_time + 1.875)
    hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.875, end=start_time + 2.25)
    hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 2.25, end=start_time + 2.625)
    hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 2.625, end=start_time + 3.0)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 3.0, end=start_time + 3.375)
    snare3 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 3.75, end=start_time + 4.125)
    hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 3.0, end=start_time + 3.375)
    hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 3.375, end=start_time + 3.75)
    hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 3.75, end=start_time + 4.125)
    hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 4.125, end=start_time + 4.5)
    kick4 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 4.5, end=start_time + 4.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 5.25, end=start_time + 5.625)
    hihat13 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 4.5, end=start_time + 4.875)
    hihat14 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 4.875, end=start_time + 5.25)
    hihat15 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 5.25, end=start_time + 5.625)
    hihat16 = pretty_midi.Note(velocity=90, pitch=42, start=start_time + 5.625, end=start_time + 6.0)
    drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8, kick3, snare3, hihat9, hihat10, hihat11, hihat12, kick4, snare4, hihat13, hihat14, hihat15, hihat16])

add_drums(1.5)

# Tenor sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 (melodic minor)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4 (come back)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
