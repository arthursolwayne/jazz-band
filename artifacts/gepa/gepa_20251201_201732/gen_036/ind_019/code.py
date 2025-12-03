
import pretty_midi

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Time per bar at 160 BPM (seconds per bar)
# 60 seconds / 160 beats per minute = 0.375 seconds per beat
# 4 beats per bar => 1.5 seconds per bar
BAR_LENGTH = 1.5
TOTAL_DURATION = 4 * BAR_LENGTH  # 6 seconds

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI drum kits are in program 0

# Create instruments
drum_inst = pretty_midi.Instrument(program=drum_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_inst, bass_inst, piano_inst, sax_inst]

# -------------------
# 1. DRUMS - Little Ray (Bar 1)
# -------------------
# Kick on 1 and 3
kick_note = pretty_midi.Note(velocity=100, pitch=35, start=0, end=0.375)
drum_inst.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=35, start=1.125, end=1.5)
drum_inst.notes.append(kick_note)

# Snare on 2 and 4
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_inst.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_inst.notes.append(snare_note)

# Hi-hat on every eighth
for i in range(0, 4):
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=(i + 1) * 0.375)
    drum_inst.notes.append(hi_hat)

# -------------------
# 2. BASS - Marcus (Bar 2)
# -------------------
# Walking line: D2 (D), F#2 (F#), G2 (G), A2 (A) with chromatic approaches
notes = [
    (pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)),  # D2
    (pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)), # F#2
    (pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625)), # G2
    (pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0)),  # A2
]
bass_inst.notes.extend(notes)

# -------------------
# 3. PIANO - Diane (Bar 3)
# -------------------
# Open voicings with different chords each bar, resolving on the last
# Bar 3: D major 7 (D, F#, A, C#)
# Bar 4: G7 (G, B, D, F)
# Use open voicings with some tension

# Bar 3 (Dmaj7) - Open voicing
d_maj7 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C#5
]
piano_inst.notes.extend(d_maj7)

# Bar 4 (G7) - Open voicing, resolving
g7 = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F4
]
piano_inst.notes.extend(g7)

# -------------------
# 4. SAX - Dante (Bar 4)
# -------------------
# Tenor sax: short motif, leave the last note hanging
# Motif: D4 (start at 2.25), F#4 (2.5), D4 (2.75) — ends with a rest
# Short, singable, unresolved

d_note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
f_sharp_note = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75)
sax_inst.notes.append(d_note)
sax_inst.notes.append(f_sharp_note)

# -------------------
# Save the MIDI
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
